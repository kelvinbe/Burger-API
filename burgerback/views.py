from django.shortcuts import render
from burgerback.models import Ingredient
from rest_framework import viewsets
from burgerback.serializers.serializers import IngredientSerializer


# Create your views here.


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    


