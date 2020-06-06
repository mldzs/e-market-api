from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import TipoProduto, Produto, ProdutoCarrinho
from .serializers import ProdutoSerializer, TipoProdutoSerializer, ProdutoCarrinhoSerializer
from ..utils.permissions import (
    EstabelecimentoPermissao,
    ProprioProdutoSupermercadoPermissao,
    ClientePermissao,
    ProprioClienteProdutoCarrinhoPermissao,
)
from ..utils.views import MixedPermissionModelViewSet


class TipoProdutoViewSet(MixedPermissionModelViewSet):
    queryset = TipoProduto.objects.all()
    serializer_class = TipoProdutoSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, EstabelecimentoPermissao],
        "partial_update": [IsAuthenticated, EstabelecimentoPermissao],
        "destroy": [IsAuthenticated, EstabelecimentoPermissao],
    }


class ProdutoViewSet(MixedPermissionModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, EstabelecimentoPermissao],
        "partial_update": [IsAuthenticated, ProprioProdutoSupermercadoPermissao],
        "destroy": [IsAuthenticated, ProprioProdutoSupermercadoPermissao],
    }

    def create(self, request, *args, **kwargs):
        estabelecimento = request.user.estabelecimento
        request.data["estabelecimento"] = estabelecimento.pk

        return super().create(request, *args, **kwargs)


class ProdutoCarrinhoViewSet(MixedPermissionModelViewSet):
    queryset = ProdutoCarrinho.objects.all()
    serializer_class = ProdutoCarrinhoSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    permission_classes_by_action = {
        "list": [IsAuthenticated, ClientePermissao],
        "retrieve": [IsAuthenticated, ClientePermissao, ProprioClienteProdutoCarrinhoPermissao],
        "create": [IsAuthenticated, ClientePermissao],
        "partial_update": [IsAuthenticated, ProprioClienteProdutoCarrinhoPermissao],
        "destroy": [IsAuthenticated, ProprioClienteProdutoCarrinhoPermissao],
    }

    def list(self, request, *args, **kwargs):
        self.queryset = ProdutoCarrinho.objects.filter(carrinho__cliente=request.user.cliente)

        return super().list(request, *args, **kwargs)
