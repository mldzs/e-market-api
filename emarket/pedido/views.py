from random import shuffle

from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
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
from ..utils.views import MixedPermissionModelViewSet


class PedidoViewSet(MixedPermissionModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    http_method_names = ["get", "post"]

    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, ClientePermissao],
    }

    def get_queryset(self):
        try:
            return Pedido.objects.filter(carrinho__cliente=self.request.user.cliente)
        except Exception:
            raise ValidationError({"message": "Você não é um cliente!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def aceitar_pedido(self, request, pk=None):
        pedido = self.get_object()
        pedido.status = "elaborando_pedido"
        pedido.save()

        # fcm_devices_cliente = request.user.fcmdevice_set.all()
        # fcm_devices_cliente.send_message(title="Title", body="Message", data={"test": "test"})
        # envio de email também
        # passar pro celery

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def rejeitar_pedido(self, request, pk=None):
        # pedido = self.get_object()
        # pedido.status = "elaborando_pedido"
        # pedido.save()

        # remover pedido???
        # pegar mensagem do estabelecimento e mandar pro cliente

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def solicitar_entregador(self, request, pk=None):
        entregadores = list(Entregador.objects.all())
        entregador = shuffle(entregadores)
        if not entregador:
            return Response({"message": "Não encontramos entregadores no momento!"})

        pedido = self.get_object()
        pedido.entregador = entregador
        pedido.status = "aguardando_entregador"
        pedido.save()

        # enviar mensagem pro entregador
        # avisar pro cliente que pedido está esperando entregador

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, PedidoEstabelecimento])
    def cancelar_solicitacao_entregador(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "aguardando_entregador":
            return Response({"message": "Esse pedido não está aguardando entregador!"})

        pedido.status = "elaborando_pedido"
        pedido.entregador = None
        pedido.save()

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, EntregadorPermissao])
    def aceitar_solicitacao_entrega(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "aguardando_entregador":
            return Response({"message": "O pedido não está pendente de entrega!"})

        pedido.status = "entregando"
        pedido.save()

        # avisar pro estabelecimento que o entregador aceitou
        # avisar pro cliente que pedido está sendo entregue

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, EntregadorPermissao])
    def rejeitar_solicitacao_entrega(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "aguardando_entregador":
            return Response({"message": "O pedido não está pendente de entrega!"})

        entregadores = list(Entregador.objects.all())
        entregador = shuffle(entregadores)
        if not entregador:
            entregador = None
            # avisar pro supermercado que não tem entregador
        else:
            pass
            # enviar mensagem pro entregador

        pedido.entregador = entregador
        pedido.status = "aguardando_entregador"
        pedido.save()

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})

    @action(methods=["PATCH"], detail=True, permission_classes=[IsAuthenticated, ProprioPedidoClientePermissao])
    def confirmar_recebimento_pedido(self, request, pk=None):
        pedido = self.get_object()

        if pedido.status != "entregando":
            return Response({"message": "Seu pedido ainda não está sendo entregue!"})

        pedido.status = "entregue"
        pedido.save()

        # notificar supermercado

        return Response({"message": "O pedido foi aceito. Avise-nos quando estiver pronto!"})
