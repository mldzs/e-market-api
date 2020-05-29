from django.contrib import admin

from ..veiculo.models import Veiculo


class VeiculoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Veiculo, VeiculoAdmin)
