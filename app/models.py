from typing import Tuple
from django.db import models

# Create your models here.

class Myprojects(models.Model):
    title = models.CharField(max_length=50)
    about = models.TextField()
    url = models.URLField(max_length=200, null=True)
    banner = models.ImageField(upload_to='banner', null = False)
    date = models.DateField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self) -> str:
        return self.title