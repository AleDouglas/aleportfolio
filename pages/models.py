from django.db import models
from django.urls import reverse


class Contato(models.Model):
    criado = models.DateField('Data do contato', auto_now_add=True)
    nome = models.CharField('Nome completo',max_length=200, blank=False)
    email = models.EmailField('Email para contato',max_length=200,blank=False)
    titulo = models.CharField('Título do assunto',max_length=200,blank=False)
    assunto = models.TextField('Assunto',blank=False)

    class Meta:
        ordering = ["-criado"]

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')


class Projeto(models.Model):
    criado = models.DateField('Postado em', auto_now_add=True)
    titulo = models.CharField('Título', max_length=200)
    conteudo = models.TextField('Conteúdo')

    def __str__(self):
        return self.titulo
