from django.views.generic import TemplateView
from .models import Post

class HomePageView(TemplateView):
    model = Post
    template_name = 'home.html'