from django.db import models

# Create your models here.

class Recipe(models.Model):
    diff = (
       ('Easy', ('1')),
       ('Medium', ('2')),
       ('Difficult', ('3')),
   )
    name = models.CharField(
        max_length=100, help_text='Name of the recipe'
    )
    time = models.PositiveIntegerField(
        help_text='Time to do this recipe in minutes'
    )
    difficulty = models.CharField(
        help_text='Difficulty of this recipe',
        max_length=32,
        choices=diff,
    )
    URL = models.URLField(
        help_text='URL wikipedia of the recipe'
    )
    origin = models.CharField(
        max_length=100, help_text='Country of the recipe'
    )

    def __str__(self):
        return self.name
