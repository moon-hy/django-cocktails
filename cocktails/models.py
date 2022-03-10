from unicodedata import name
from django.db import models

# Create your models here.
class CocktailBase(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class CocktailTechnique(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey('Cocktail', on_delete=models.CASCADE, related_name='ingredient_volume', blank=True)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE, related_name='ingredient_volume')
    volume = models.PositiveSmallIntegerField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cocktail} {self.ingredient} {self.volume} {self.unit}'

class Cocktail(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    base = models.ForeignKey('CocktailBase', db_index=True, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(
        'ingredients.Ingredient', through='CocktailIngredient', related_name='cocktails'
    )
    garnish = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['base', 'name']

    def __str__(self):
        return self.name
