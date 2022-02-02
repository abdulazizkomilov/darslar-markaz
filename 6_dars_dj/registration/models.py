from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Reclama(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    summary = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(
        'auth.User',

        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

    
    
    
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    
