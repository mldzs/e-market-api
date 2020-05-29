from django.db import models

from ..produto.models import ProdutoCarrinho
from ..usuario.models import Cliente


class Carrinho(models.Model):
    produto_carrinho = models.ManyToManyField(ProdutoCarrinho)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="carrinhos")
