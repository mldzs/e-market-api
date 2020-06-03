from rest_framework import serializers
from rest_framework.fields import empty

from .models import TipoProduto, ProdutoCarrinho, Produto
from ..usuario.serializers import EstabelecimentoSerializer


class TipoProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoProduto
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)

        try:
            if self.context["request"].method == "GET":
                self.fields["estabelecimento"] = EstabelecimentoSerializer()
                self.fields["tipo_produto"] = TipoProdutoSerializer()
        except KeyError:
            pass


"""class Test:
    requires_context = True

    def __call__(self, value, serializer_field):
        estabelecimento_produto = value.estabelecimento
        print(dir(serializer_field.get_value()))
        # serializer_field.context["request"].carrinho
        # pegar supermercado do carrinh e comparar com o do produto. CAso sejam diferentes, validation error
        #print(dir(serializer_field))
        #print()"""


class ProdutoCarrinhoSerializer(serializers.ModelSerializer):
    # produto = serializers.PrimaryKeyRelatedField(validators=[Test()], queryset=Produto.objects.all())

    class Meta:
        model = ProdutoCarrinho
        fields = '__all__'

    def create(self, validated_data):
        ...
