from django.db.models import Count
from rest_framework import viewsets
from .constants import GetParams, MatchLevel
from .models import Ingredient, Seasoning, Recipe
from .serializers import IngredientSerializer, SeasoningSerializer, RecipeSerializer
from itertools import chain
# Create your views here.


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        return self.queryset if name is None else self.queryset.filter(name=name)

class CondimentViewSet(viewsets.ModelViewSet):
    queryset = Seasoning.objects.all()
    serializer_class = SeasoningSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        ingredients = self.get_request_list(GetParams.INGREDIENTS)
        seasonings = self.get_request_list(GetParams.SEASONING)

        if ingredients is None:
            return self.queryset

        if seasonings is None:
            return self.filter_ingredients(ingredients)

        return self.filter_both(ingredients, seasonings)

    def get_request_list(self, param):
        raw = self.request.query_params.get(param, None)
        return raw.split('|') if raw is not None else None

    def filter_ingredients(self, ingredients):
        '''
        Filters the recipe on the exact given ingredients having any seasonings.
        :param ingredients: list of ingredients
        :return: matching recipes
        '''
        result_set = self.queryset.filter(ingredients__name__in=ingredients)\
                        .order_by('name')\
                        .distinct()

        if self.is_match_any_ingredients():
            return result_set

        return result_set.annotate(total=Count('ingredients'))\
            .filter(total=len(ingredients))\
            .distinct()

    def is_match_any_ingredients(self):
        return self.get_looseness() == MatchLevel.INGREDIENTS_ONLY

    def get_looseness(self):
        return self.request.query_params.get(GetParams.MATCH_ANY_LEVEL, None)

    def filter_both(self, ingredients, seasonings):
        ingredient_set = self.queryset.filter(ingredients__name__in=ingredients).distinct()

        if self.is_match_any_both():
            seasoning_set = self.queryset.filter(seasonings__name__in=seasonings).distinct()
            return list(set(chain(ingredient_set, seasoning_set)))

        if self.is_match_any_ingredients():
            return self.filter_exact_seasonings(seasonings, ingredient_set)

        results = self.queryset.filter(ingredients__name__in=ingredients)\
                        .filter(seasonings__name__in=seasonings)\
                        .distinct()

        return results if self.is_match_any_seasoning() else self.filter_exact_seasonings(seasonings, results)

    def filter_exact_seasonings(self, seasonings, results):
        return [result for result in results if seasonings == [s.name for s in result.seasonings.all()]]

    def is_match_any_both(self):
        return self.get_looseness() == MatchLevel.BOTH

    def is_match_any_seasoning(self):
        return self.get_looseness() == MatchLevel.SEASONING_ONLY

