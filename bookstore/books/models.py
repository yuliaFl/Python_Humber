from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    year = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True) 
    def __str__(self):
        return self.title


