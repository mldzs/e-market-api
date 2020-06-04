from rest_framework import serializers
from rest_framework.fields import empty

from .models import TipoProduto, ProdutoCarrinho, Produto
from ..usuario.serializers import EstabelecimentoSerializer


class TipoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProduto
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        try:
            if self.context["request"].method == "GET":
                self.fields["estabelecimento"] = EstabelecimentoSerializer()
                self.fields["tipo_produto"] = TipoProdutoSerializer()
        except KeyError:
            pass


class ProdutoCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoCarrinho
        fields = "__all__"
