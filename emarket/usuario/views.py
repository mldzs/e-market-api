from rest_framework.viewsets import ModelViewSet

from .serializers import EnderecoSerializer, EstabelecimentoSerializer, ClienteSerializer, EntregadorSerializer
from .models import Endereco, Estabelecimento, Cliente, Entregador


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class EstabelecimentoViewSet(ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class EntregadorViewSet(ModelViewSet):
    queryset = Entregador.objects.all()
    serializer_class = EntregadorSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
