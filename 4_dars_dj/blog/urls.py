from django.urls import path
from .views import HomePageView, ListDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', ListDetailView.as_view(), name='post_detail'),  # yangilik
]