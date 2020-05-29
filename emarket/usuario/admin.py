from django.contrib import admin

from .models import Cliente, Estabelecimento, Endereco, Entregador


class EnderecoAdmin(admin.ModelAdmin):
    pass


class EstabelecimentoAdmin(admin.ModelAdmin):
    pass


class ClienteAdmin(admin.ModelAdmin):
    pass


class EntregadorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Entregador, EntregadorAdmin)
