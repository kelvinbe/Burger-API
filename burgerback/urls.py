from burgerback.views import IngredientViewSet
from django.urls import path


ingredients_list = IngredientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', ingredients_list, name='ingredient-list')
]
