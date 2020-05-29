# Generated by Django 3.0.6 on 2020-05-29 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('veiculo', '0002_auto_20200529_0129'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=60)),
                ('bairro', models.CharField(max_length=60)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=16)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estabelecimentos', to='usuario.Endereco')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estabelecimentos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'estabelecimentos',
            },
        ),
        migrations.CreateModel(
            name='Entregador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='veiculo.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.Endereco')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]