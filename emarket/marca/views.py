from rest_framework.permissions import IsAuthenticated

from .serializers import MarcaSerializer
from .models import Marca
from ..utils.permissions import EstabelecimentoPermissao
from ..utils.views import MixedPermissionModelViewSet


class MarcaViewSet(MixedPermissionModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated, EstabelecimentoPermissao],
        "partial_update": [IsAuthenticated, EstabelecimentoPermissao],
        "destroy": [IsAuthenticated, EstabelecimentoPermissao],
    }
