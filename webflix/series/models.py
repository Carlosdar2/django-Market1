from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import IntegerField

# Create your models here.
class Serie(models.Model):

    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action' 
    DRAMA  = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR,'Horror'),
        (COMEDY,'comedy'),
        (ACTION,'Action'),
        (DRAMA, 'Drama'),

    )

    name = models.CharField(max_length=100)
    release = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=50,choices=CATEGORIES_CHOICES)
