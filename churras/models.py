from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

#from pessoas.models import Pessoa

# Está classe de models se tornará uma tabela no banco de dados
class Prato(models.Model):
    # Serão os campos da tabela, ou seja, atributos da classe

    CATEGORIA_CHOICES = (
        ('Churrasco','Churrasco'),
        ('Entrada','Entrada'),
        ('Sobremesa','Sobremesa'),
    )

    pessoa = models.ForeignKey(User, on_delete = models.CASCADE)

    nome_prato = models.CharField(
        max_length=100,
        verbose_name="Nome do Prato",
    )
    ingredientes = models.TextField(
        verbose_name='Ingredientes',
    )
    modo_preparo = models.TextField(
        verbose_name = 'Modo de Preparo',
    )
    tempo_preparo = models.PositiveIntegerField(
        verbose_name = 'Tempo de Preparo',
    )
    rendimento = models.CharField(max_length=100,
        verbose_name = 'Rendimento',
    )
    categoria = models.CharField(max_length=100,
        verbose_name = 'Categoria',
        choices=CATEGORIA_CHOICES,
    )
    date_prato = models.DateTimeField(
        default = datetime.now, blank = True
    )

    foto_prato = models.ImageField(
        upload_to='pratos/%Y/%m',
        blank=True
    )

    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_prato
    
    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Pratos'