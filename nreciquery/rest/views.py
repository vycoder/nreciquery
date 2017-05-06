from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ingredient, Condiment, Recipe
from .serializers import IngredientSerializer, CondimentSerializer, RecipeSerializer
# Create your views here.


class IngredientList(APIView):

    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
