from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Reclama

class BlogListView(ListView):
    model = Reclama
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Reclama
    template_name = 'post_detail.html'

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
