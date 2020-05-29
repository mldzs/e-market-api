from rest_framework import serializers

from .models import TipoProduto, ProdutoCarrinho, Produto


class TipoProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoProduto
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoCarrinhoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProdutoCarrinho
        fields = '__all__'
