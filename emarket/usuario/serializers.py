from rest_framework import serializers

from .models import Endereco, Estabelecimento, Cliente, Entregador


class UserAbstractSerializer(serializers.ModelSerializer):
    ...


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class EstabelecimentoSerializer(UserAbstractSerializer):
    class Meta:
        model = Estabelecimento
        fields = "__all__"


class ClienteSerializer(UserAbstractSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class EntregadorSerializer(UserAbstractSerializer):
    class Meta:
        model = Entregador
        fields = "__all__"
