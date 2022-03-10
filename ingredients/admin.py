from django.contrib import admin
from ingredients.models import Ingredient, IngredientCategory
# Register your models here.
admin.site.register(IngredientCategory)
admin.site.register(Ingredient)
