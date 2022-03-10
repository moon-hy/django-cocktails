from django.db import models

# Create your models here.
class IngredientCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey('IngredientCategory', on_delete=models.SET('deleted'))
    abv = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
