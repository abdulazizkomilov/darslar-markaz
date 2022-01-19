from django.urls import path
from .views import BlogListView, BlogDetailView, SignUpView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(),name='signup'),
]