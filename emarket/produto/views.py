from rest_framework.viewsets import ModelViewSet

from .models import TipoProduto, Produto, ProdutoCarrinho
from .serializers import ProdutoSerializer, TipoProdutoSerializer, ProdutoCarrinhoSerializer


class TipoProdutoViewSet(ModelViewSet):
    queryset = TipoProduto.objects.all()
    serializer_class = TipoProdutoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class ProdutoCarrinhoViewSet(ModelViewSet):
    queryset = ProdutoCarrinho.objects.all()
    serializer_class = ProdutoCarrinhoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
