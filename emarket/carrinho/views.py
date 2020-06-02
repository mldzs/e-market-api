from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CarrinhoSerializer
from .models import Carrinho
from ..utils.permissions import ProprioCarrinhoClientePermissao, ClientePermissao
from ..utils.views import MixedPermissionModelViewSet


class CarrinhoViewSet(MixedPermissionModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated, ProprioCarrinhoClientePermissao],
        "create": [IsAuthenticated, ClientePermissao],
        "partial_update": [IsAuthenticated, ProprioCarrinhoClientePermissao],
        "destroy": [IsAuthenticated, ProprioCarrinhoClientePermissao],
    }

    def list(self, request, *args, **kwargs):
        try:
            self.queryset = Carrinho.objects.filter(cliente=request.user.cliente)
        except:
            return Response({"message": "Você não tem permissão de Cliente."}, 400)

        return super().list(*args, **kwargs)
