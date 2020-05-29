from django.db import models


class Veiculo(models.Model):
    placa = models.CharField(max_length=50)
    ano = models.IntegerField()
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)

    class Meta:
        db_table = 'veiculo'
