from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib import messages
from .models import *

class HomePageView(CreateView):
    model = Contato
    fields = ['nome','email','titulo', 'assunto']
    template_name = 'paginas/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Formulário de contato enviado com sucesso!')
        return super(HomePageView, self).form_valid(form)