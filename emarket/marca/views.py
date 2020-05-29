from rest_framework.viewsets import ModelViewSet

from .serializers import MarcaSerializer
from .models import Marca


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
