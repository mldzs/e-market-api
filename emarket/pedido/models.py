from django.db import models

from ..carrinho.models import Carrinho
from ..usuario.models import Entregador


STATUS_PEDIDO = (("", ""), ("", ""), ("", ""))


class Pedido(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.PROTECT, related_name='pedidos')
    status = models.CharField(max_length=100, choices=STATUS_PEDIDO)
    entregador = models.ForeignKey(Entregador, on_delete=models.PROTECT, related_name='pedidos')
