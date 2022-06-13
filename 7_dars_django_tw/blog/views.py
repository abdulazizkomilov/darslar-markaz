from django.shortcuts import render
from django.views.generic import TemplateView

class BlogListView(TemplateView):
    template_name = 'index.html'

