from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(
        max_length=100, help_text='Name of the recipe'
    )
    time = models.PositiveIntegerField(
        help_text='Time to do this recipe in minutes'
    )
    difficulty = models.PositiveIntegerField(
        help_text='Difficulty of this recipe'
    )
    URL = models.URLField(
        help_text='URL wikipedia of the recipe'
    )
    origin = models.CharField(
        max_length=100, help_text='Country of the recipe'
    )
    
    def __str__(self):
        return self.name
