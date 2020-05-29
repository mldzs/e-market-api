from rest_framework.viewsets import ModelViewSet

from .models import Pedido
from .serializers import PedidoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
