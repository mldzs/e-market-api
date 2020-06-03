from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Pedido
from .serializers import PedidoSerializer
from ..utils.permissions import ProprioPedidoClientePermissao, ClientePermissao
from ..utils.views import MixedPermissionModelViewSet


class PedidoViewSet(MixedPermissionModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    http_method_names = ['get', 'post']

    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated, ProprioPedidoClientePermissao],
        "create": [IsAuthenticated, ClientePermissao]
    }

    def list(self, request, *args, **kwargs):
        try:
            self.queryset = Pedido.objects.filter(carrinho__cliente=request.user.cliente)
        except:
            return Response({"message": "Você não tem permissão de Cliente."}, 400)

        return super().list(*args, **kwargs)
