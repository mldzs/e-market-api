from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import VeiculoSerializer
from .models import Veiculo
from ..utils.permissions import EntregadorPermissao, DonoDoVeiculoPermissao
from ..utils.views import MixedPermissionModelViewSet


class VeiculoViewSet(MixedPermissionModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    permission_classes_by_action = {
        "list": [IsAuthenticated, EntregadorPermissao],
        "retrieve": [IsAuthenticated, DonoDoVeiculoPermissao],
        "create": [IsAuthenticated, EntregadorPermissao],
        "partial_update": [IsAuthenticated, DonoDoVeiculoPermissao],
        "destroy": [IsAuthenticated, DonoDoVeiculoPermissao],
    }

    def list(self, request, *args, **kwargs):
        self.queryset = Veiculo.objects.filter(entregador=request.user.entregador)

        return super().list(request, *args, **kwargs)
