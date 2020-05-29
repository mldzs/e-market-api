from django.contrib import admin

from .models import Carrinho


class CarrinhoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Carrinho, CarrinhoAdmin)
