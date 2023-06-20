from django.contrib import admin
from .models import Pessoa


# Register your models here.
class ListandoPessoas(admin.ModelAdmin):
    list_display = [
        'id', 'nome','email'
    ]
    list_display_links = [
        'nome', 'id'
    ]
    search_fields = ['nome']
    list_editables = ['email']
    ordering = ['-id',]
    list_filter = ['email']
    list_per_page = 7
admin.site.register(Pessoa, ListandoPessoas)