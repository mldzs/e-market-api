from rest_framework.viewsets import ModelViewSet

from .serializers import CategoriaSerializer
from .models import Categoria


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
