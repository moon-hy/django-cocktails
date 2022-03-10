from rest_framework import serializers
from cocktails.models import (
    Cocktail, CocktailBase, CocktailIngredient
)

class CocktailBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CocktailBase
        fields = '__all__'

class CocktailIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CocktailIngredient
        fields = '__all__'
        
class CocktailSerializer(serializers.ModelSerializer):
    ingredients = CocktailIngredientSerializer(source='ingredient_volume', many=True)
    abv = serializers.SerializerMethodField(method_name='get_abv')

    class Meta:
        model = Cocktail
        fields = '__all__'
        
    def create(self, validated_data):
        ingredients = validated_data.pop('ingredient_volume', [])
        tags = validated_data.pop('tags',[])

        cocktail = Cocktail.objects.create(**validated_data)
        for ingredient in ingredients:
            """ Create Middle Table """
            CocktailIngredient.objects.create(
                cocktail=cocktail, **ingredient,
            ).save()

        for tag in tags:
            """ Add ManyToMany Tag """
            cocktail.tags.add(tag)

        return cocktail


    def get_abv(self, instance):
        total_volume = 1
        total_alcohol = 0

        for ingredient in instance.ingredient_volume.all():
            total_alcohol += ingredient.volume*ingredient.ingredient.abv 
            total_volume += ingredient.volume

        return round(total_alcohol/total_volume, 2)
