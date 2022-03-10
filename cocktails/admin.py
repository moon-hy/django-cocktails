from django.contrib import admin

from cocktails.models import Cocktail, CocktailBase, CocktailIngredient, CocktailTechnique, Unit
# Register your models here.

class CocktailIngredientInline(admin.TabularInline):
    model = CocktailIngredient
    extra = 3

class CocktailAdmin(admin.ModelAdmin):
    inlines = (CocktailIngredientInline,)

admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailBase)
admin.site.register(CocktailIngredient)
admin.site.register(Unit)
admin.site.register(CocktailTechnique)
