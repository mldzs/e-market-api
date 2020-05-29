from django.contrib import admin

from .models import TipoProduto, Produto, ProdutoCarrinho


class TipoProdutoAdmin(admin.ModelAdmin):
    pass


class ProdutoAdmin(admin.ModelAdmin):
    pass


class ProdutoCarrinhoAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoProduto, TipoProdutoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ProdutoCarrinho, ProdutoCarrinhoAdmin)
