from django.db import models

from ..carrinho.models import Carrinho
from ..usuario.models import Entregador


STATUS_PEDIDO = (
    ("pendente", "Pendente"),
    ("elaborando_pedido", "Elaborando Pedido"),
    ("aguardando_entregador", "Aguardando Entregador"),
    ("entregando", "Entregando"),
    ("entregue", "Entregue"),
)


class Pedido(models.Model):
    carrinho = models.OneToOneField(Carrinho, on_delete=models.PROTECT, related_name="pedidos")
    status = models.CharField(max_length=100, choices=STATUS_PEDIDO, default="pendente")
    entregador = models.OneToOneField(
        Entregador, on_delete=models.PROTECT, related_name="pedidos", blank=True, null=True
    )
