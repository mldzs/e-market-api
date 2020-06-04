from rest_framework import serializers

from .models import Pedido
from .validators import MesmoUsuarioCarrinhoERequisicao
from ..carrinho.models import Carrinho


class PedidoSerializer(serializers.ModelSerializer):
    carrinho = serializers.PrimaryKeyRelatedField(
        queryset=Carrinho.objects.all(), validators=[MesmoUsuarioCarrinhoERequisicao()]
    )

    class Meta:
        model = Pedido
        fields = "__all__"
        read_only_fields = ["status"]
