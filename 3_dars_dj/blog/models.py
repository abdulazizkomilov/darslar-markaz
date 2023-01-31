from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    summury = models.CharField(max_length=150, blank=True)  # yangilik
    text = models.TextField()

    #admin panelda postlarni nomini ko`rsatadi
    def __str__(self):
        return self.title

    #postlarni primary key larini qaytaradi
    def get_absolute_url(self): # yangilik
        return reverse("post_detail", args={str(self.pk)})
    