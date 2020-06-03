from django.db import models

from ..usuario.models import Cliente, Estabelecimento


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="carrinhos")
    estabelecimento = models.OneToOneField(Estabelecimento, on_delete=models.CASCADE, related_name="carrinhos")
