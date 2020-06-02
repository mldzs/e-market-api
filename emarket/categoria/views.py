from rest_framework.permissions import IsAuthenticated

from .serializers import CategoriaSerializer
from .models import Categoria
from ..utils.permissions import EstabelecimentoPermissao
from ..utils.views import MixedPermissionModelViewSet


class CategoriaViewSet(MixedPermissionModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, EstabelecimentoPermissao],
        "partial_update": [IsAuthenticated, EstabelecimentoPermissao],
        "destroy": [IsAuthenticated, EstabelecimentoPermissao],
    }
