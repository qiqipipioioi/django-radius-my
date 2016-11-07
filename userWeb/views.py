from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = "userWeb/index.html"
    context_object_name = "index"
    def get_queryset(self):
        return
# Create your views here.
