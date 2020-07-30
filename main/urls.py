from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register("ingredients", views.IngredientViewSet)
router.register("dishes", views.DishViewSet)
router.register("recipes", views.RecipeViewSet)
router.register("Quantity", views.QuantityViewSet)


urlpatterns = [
    path("", include(router.urls))
]
