from rest_framework import serializers
from .models import Ingredient, Condiment, Recipe


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        field = ('name')


class CondimentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condiment
        field = ('name')


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        field = (
            'name',
            'description',
            'type',
            'ingredients',
            'condiments',
            'ingredients_details',
            'directions'
        )