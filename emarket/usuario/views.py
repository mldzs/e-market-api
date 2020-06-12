from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import EnderecoSerializer, EstabelecimentoSerializer, ClienteSerializer, EntregadorSerializer
from .models import Endereco, Estabelecimento, Cliente, Entregador


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    http_method_names = ["get", "post", "patch", "delete"]


class EstabelecimentoViewSet(ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    http_method_names = ["get", "post", "patch", "delete"]


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ["get", "post", "patch", "delete"]


class EntregadorViewSet(ModelViewSet):
    queryset = Entregador.objects.all()
    serializer_class = EntregadorSerializer
    http_method_names = ["get", "post", "patch", "delete"]


class TokenLogin(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        user = User.objects.get(username=request.data.get("username"))

        if hasattr(user, "cliente"):
            tipo_usuario = "cliente"
        elif hasattr(user, "estabelecimento"):
            tipo_usuario = "estabelecimento"
        else:
            tipo_usuario = "entregador"

        response.data["tipo_usuario"] = tipo_usuario
        return response
