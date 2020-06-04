from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=55)
    imagem = models.ImageField(upload_to="marcas/")

    class Meta:
        db_table = "marca"
