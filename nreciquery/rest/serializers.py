from rest_framework import serializers
from .models import Ingredient, Condiment, Recipe


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name',)


class CondimentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condiment
        fields = ('name',)


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = (
            'name',
            'description',
            'type',
            'ingredients',
            'condiments',
            'ingredients_details',
            'directions'
        )