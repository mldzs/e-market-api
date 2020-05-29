from django.contrib import admin

from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categoria, CategoriaAdmin)
