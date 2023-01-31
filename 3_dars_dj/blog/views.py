from django.views.generic import ListView, DetailView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class ListDetailView(DetailView):  # yangilik
    model = Post
    template_name = 'post_detail.html'
    feilds = ['title', 'summury', 'text']
