from rest_framework.viewsets import ModelViewSet

from .serializers import CarrinhoSerializer
from .models import Carrinho


class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
