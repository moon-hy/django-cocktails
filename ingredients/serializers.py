from rest_framework import serializers
from .models import Ingredient, IngredientCategory


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
