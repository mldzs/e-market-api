from rest_framework.permissions import IsAuthenticated

from .serializers import CarrinhoSerializer
from .models import Carrinho
from ..utils.permissions import ProprioCarrinhoClientePermissao, ClientePermissao
from ..utils.views import MixedPermissionModelViewSet


class CarrinhoViewSet(MixedPermissionModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    http_method_names = ["get", "post", "delete"]

    permission_classes_by_action = {
        "list": [IsAuthenticated, ClientePermissao],
        "retrieve": [IsAuthenticated, ProprioCarrinhoClientePermissao],
        "create": [IsAuthenticated, ClientePermissao],
        "destroy": [IsAuthenticated, ProprioCarrinhoClientePermissao],
    }

    def list(self, request, *args, **kwargs):
        self.queryset = Carrinho.objects.filter(cliente=self.request.user.cliente)

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        cliente = request.user.cliente
        request.data["cliente"] = cliente.pk

        return super().create(request, *args, **kwargs)
