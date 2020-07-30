from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

# Create your views here.


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = models.Ingredient.objects.all()


class DishViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DishSerializer
    queryset = models.Dish.objects.all()


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = models.Recipe.objects.all()


class QuantityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuantitySerializer
    queryset = models.Quantity.objects.all()
