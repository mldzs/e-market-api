from django.db import models

from ..usuario.models import Cliente


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="carrinhos")
