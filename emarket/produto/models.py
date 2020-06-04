from django.db import models
from rest_framework.exceptions import ValidationError

from ..carrinho.models import Carrinho
from ..categoria.models import Categoria
from ..marca.models import Marca
from ..usuario.models import Estabelecimento


class TipoProduto(models.Model):
    nome = models.CharField(max_length=200)
    peso = models.FloatField()
    imagem = models.ImageField(upload_to="tipos_produto/")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="tipos_produto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="tipos_produto")


class Produto(models.Model):
    tipo_produto = models.ForeignKey(TipoProduto, on_delete=models.CASCADE, related_name="produtos")
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name="produtos")
    preco = models.FloatField()


class ProdutoCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="produtos_carrinho")
    quantidade = models.PositiveIntegerField()
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="produtos_carrinho")

    def clean(self):
        if self.produto.estabelecimento != self.carrinho.estabelecimento:
            raise ValidationError("O produto deve pertencer ao estabelecimento do carrinho!")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_clean()
        super().save(force_insert, force_update, using, update_fields)
