from django.db import models

# Create your models here.
from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.recipe_name