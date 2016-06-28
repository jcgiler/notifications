from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ContentView(TemplateView):
    template_name = 'alert/content.html'
