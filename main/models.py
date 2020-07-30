from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    weight = models.IntegerField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    # get name, weight and description from parent Ingredient class
    effect = models.TextField()
    ingredient = models.OneToOneField(
        "Ingredient", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    min_skill = models.CharField(max_length=32)
    skill_num = models.IntegerField()

    dish = models.OneToOneField(
        "Dish", on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(
        "Ingredient", through="Quantity", related_name="recipes")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Quantity(models.Model):
    amount = models.IntegerField()

    recipe = models.ForeignKey(
        "Recipe", on_delete=models.SET_NULL, null=True, related_name="quantity")
    ingredient = models.ForeignKey(
        "Ingredient", on_delete=models.SET_NULL, null=True, blank=True, related_name="quantity")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
