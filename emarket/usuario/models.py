from django.contrib.auth.models import User
from django.db import models

from ..veiculo.models import Veiculo


class Endereco(models.Model):
    estado = models.CharField(max_length=10)
    cidade = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)


class Estabelecimento(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=16)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)

    class Meta:
        default_related_name = "estabelecimento"


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)

    default_related_name = "cliente"


class Entregador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    veiculo = models.OneToOneField(Veiculo, on_delete=models.PROTECT, blank=True, null=True)

    default_related_name = "entregador"
