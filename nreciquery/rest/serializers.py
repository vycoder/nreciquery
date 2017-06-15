from rest_framework import serializers
from .models import Ingredient, Seasoning, Recipe


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name',)


class SeasoningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seasoning
        fields = ('name',)


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = (
            'name',
            'description',
            'image',
            'type',
            'ingredients',
            'seasonings',
            'ingredients_details',
            'directions'
        )
        depth = 2