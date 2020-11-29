from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import *

class Bosh_Sahifa(ListView):
    template_name = 'main/index.html'
    model = Yangiliklar
    context_object_name = 'yangilik'

class Biz_Haqimizda(TemplateView):
    template_name = 'main/about.html'

class Galereya(ListView):
    template_name = 'main/gallery.html'
    model = Galereya
    context_object_name = 'galereyalar'

class Xizmatlarimiz(ListView):
    template_name = 'main/service.html'
    model = Service
    context_object_name = 'xizmat'

class Aloqa(TemplateView):
    template_name = 'main/aloqa.html'