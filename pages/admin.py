from django.contrib import admin
from .models import *


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('email', 'titulo')

admin.site.register(Contato, ContatoAdmin)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

admin.site.register(Projeto, ProjetoAdmin)