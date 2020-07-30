from rest_framework import serializers
from . import models


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ["name", "weight", "description"]


class DishSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = models.Dish
        fields = ["effect", "ingredient"]


class RecipeSerializer(serializers.ModelSerializer):
    dish = DishSerializer(many=False, read_only=True)

    class Meta:
        model = models.Recipe
        fields = ["name", "min_skill", "skill_num", "dish"]


class QuantitySerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    recipe = RecipeSerializer(many=False, read_only=False)

    class Meta:
        model = models.Quantity
        fields = ["amount", "ingredients", "recipe"]
