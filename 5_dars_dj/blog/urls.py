from django.urls import path
from .views import BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView, BlogCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogCreateView.as_view(), name='create'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('post/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('post/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]