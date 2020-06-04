from rest_framework.exceptions import ValidationError
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
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated, ProprioCarrinhoClientePermissao],
        "create": [IsAuthenticated, ClientePermissao],
        "destroy": [IsAuthenticated, ProprioCarrinhoClientePermissao],
    }

    def get_queryset(self):
        try:
            return Carrinho.objects.filter(cliente=self.request.user.cliente)
        except Exception:
            raise ValidationError({"message": "Você não tem permissão de Cliente."})

    def create(self, request, *args, **kwargs):
        cliente = request.user.cliente
        request.data["cliente"] = cliente.pk

        return super().create(request, *args, **kwargs)
