from django.db import models
from django.urls import reverse

# Create your models here.
class Knife(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    description = models.TextField(max_length=1500)
    size = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'knife_id': self.id})