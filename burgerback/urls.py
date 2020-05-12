from burgerback.views import IngredientViewSet
from django.urls import path


ingredients_list = IngredientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

ingredients_detail = IngredientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('ingredients/', ingredients_list, name='ingredient-list'),
    path('ingredients/<int:pk>/',  ingredients_detail, name='ingredient-detail')
]
