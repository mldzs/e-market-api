from random import shuffle, choice

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Pedido
from .serializers import PedidoSerializer
from ..usuario.models import Entregador
from ..utils.permissions import (
    ClientePermissao,
    PedidoEstabelecimento,
    EntregadorPermissao,
    ProprioPedidoClientePermissao,
)
from ..utils.tasks import enviar_email, enviar_notificacao
from ..utils.views import MixedPermissionModelViewSet


class PedidoViewSet(MixedPermissionModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    http_method_names = ["get", "patch", "post"]

    permission_classes_by_action = {
        "list": [IsAuthenticated, ClientePermissao],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, ClientePermissao],
    }

    def list(self, request, *args, **kwargs):
        self.queryset = Pedido.objects.filter(carrinho__cliente=self.request.user.cliente)

        return super().list(request, *args, **kwargs)

    @action(methods=["patch"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def aceitar_pedido(self, request, pk=None):
        pedido = self.get_object()
        if pedido.status != "pendente":
            return Response({"message": "O pedido não está pendente!"})

        pedido.status = "elaborando_pedido"
        pedido.save()

        cliente = pedido.carrinho.cliente.usuario
        estabelecimento = request.user

        mensagem = f"O estabelecimento {estabelecimento.first_name} aceitou sua solicitação de pedido."

        enviar_email.delay(
            to=[cliente.email],
            subject="Pedido aceito",
            context={"mensagem": mensagem},
            template="email/enviar_email.html",
        )

        enviar_notificacao.delay(id_usuarios=[cliente.pk], title="Pedido", body=mensagem)

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def rejeitar_pedido(self, request, pk=None):
        pedido = self.get_object()
        cliente = pedido.carrinho.cliente.usuario
        pedido.delete()

        mensagem_estabelecimento = request.data.get("mensagem")
        mensagem = (
            f"Seu pedido foi rejeitado. O estabelecimento deixou a seguinte mensagem: {mensagem_estabelecimento}"
        )

        enviar_email.delay(
            to=[cliente.email],
            subject="Solicitação de entrega",
            context={"mensagem": mensagem},
            template="email/enviar_email.html",
        )

        enviar_notificacao.delay(id_usuarios=[cliente.pk], title="Entrega", body=mensagem)

        return Response({"message": "O pedido foi rejeitado."})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def solicitar_entregador(self, request, pk=None):
        pedido = self.get_object()
        if pedido.status != "elaborando_pedido":
            return Response({"message": "O pedido não está sendo elaborado!"})

        entregadores = list(Entregador.objects.all())
        entregador = choice(entregadores)

        if not entregador:
            return Response({"message": "Não encontramos entregadores no momento!"})

        pedido.entregador = entregador
        pedido.status = "aguardando_entregador"
        pedido.save()

        mensagem = f"Acaba de chegar uma entrega para você realizar."

        enviar_email.delay(
            to=[entregador.usuario.email],
            subject="Solicitação de entrega",
            context={"mensagem": mensagem},
            template="email/enviar_email.html",
        )

        enviar_notificacao.delay(id_usuarios=[entregador.usuario.pk], title="Entrega", body=mensagem)

        return Response({"message": "Entrega solicitada"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def cancelar_solicitacao_entregador(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "aguardando_entregador":
            return Response({"message": "Esse pedido não está aguardando entregador!"})

        pedido.status = "elaborando_pedido"
        pedido.entregador = None
        pedido.save()

        return Response({"message": "Solicitação cancelada"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, EntregadorPermissao])
    def aceitar_solicitacao_entrega(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "aguardando_entregador":
            return Response({"message": "O pedido não está pendente de entrega!"})

        pedido.status = "entregando"
        pedido.save()

        mensagem = f"O pedido está sendo entregue."

        estabelecimento = pedido.carrinho.estabelecimento.usuario
        cliente = pedido.carrinho.cliente.usuario

        enviar_email.delay(
            to=[estabelecimento.email, cliente.email],
            subject="Solicitação de entrega",
            context={"mensagem": mensagem},
            template="email/enviar_email.html",
        )

        enviar_notificacao.delay(id_usuarios=[estabelecimento.pk, cliente.pk], title="Entrega", body=mensagem)

        return Response({"message": "A solicitação foi aceita. Já pode buscar o pedido!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, EntregadorPermissao])
    def rejeitar_solicitacao_entrega(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "aguardando_entregador":
            return Response({"message": "O pedido não está pendente de entrega!"})

        entregador_que_rejeitou = request.user.entregador
        entregadores = list(Entregador.objects.all().exclude(pk=entregador_que_rejeitou.pk))
        entregador = choice(entregadores) if entregadores else None

        if not entregador:
            entregador = None
            mensagem = """O entregador rejeitou a entrega. Tentemos achar outro mas não encontramos no momento.
                            Tente novamente daqui a pouco"""
            pedido.status = "elaborando_pedido"
        else:
            mensagem = "O entregador rejeitou a entrega. Solicitamos para outro entregador."
            pedido.status = "aguardando_entregador"

        estabelecimento = pedido.carrinho.estabelecimento.usuario
        enviar_email.delay(
            to=[estabelecimento.email],
            subject="Entrega rejeitada",
            context={"mensagem": mensagem},
            template="email/enviar_email.html",
        )
        enviar_notificacao.delay(id_usuarios=[estabelecimento.pk], title="Entrega", body=mensagem)

        pedido.entregador = entregador
        pedido.save()

        return Response({"message": "A entrega foi rejeitada."})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, ProprioPedidoClientePermissao])
    def confirmar_recebimento_pedido(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "entregando":
            return Response({"message": "Seu pedido ainda não está sendo entregue!"})

        pedido.status = "entregue"
        pedido.save()

        mensagem = "O cliente confirmou o recebimento da entrega."
        estabelecimento = pedido.carrinho.estabelecimento.usuario
        enviar_email.delay(
            to=[estabelecimento.email],
            subject="Entrega confirmada",
            context={"mensagem": mensagem},
            template="email/enviar_email.html",
        )

        enviar_notificacao.delay(id_usuarios=[estabelecimento.pk], title="Entrega", body=mensagem)

        return Response({"message": "Entrega confirmada!"})
