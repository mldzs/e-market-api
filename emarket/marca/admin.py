from django.contrib import admin

from .models import Marca


class MarcaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Marca, MarcaAdmin)
