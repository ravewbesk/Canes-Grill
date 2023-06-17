# Generated by Django 4.2.2 on 2023-06-16 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prato', models.CharField(max_length=100, verbose_name='Nome do Prato')),
                ('ingredientes', models.TextField(verbose_name='Ingredientes')),
                ('modo_preparo', models.TextField(verbose_name='Modo de Preparo')),
                ('tempo_preparo', models.PositiveIntegerField(verbose_name='Tempo de Preparo')),
                ('rendimento', models.CharField(max_length=100, verbose_name='Rendimento')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('date_prato', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
