from operator import mod
from pyexpat import model
from django.db import models
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=200)
    summury = models.CharField(max_length=150, blank=True)  # yangilik
    text = models.TextField()

    def __str__(self):
        return self.title


    def get_absolute_url(self): # yangilik
        return reverse("post_detail", args={str(self.pk)})
    