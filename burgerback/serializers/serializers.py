from rest_framework import serializers
from burgerback.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'price']

    def create(self, validated_data):
        return Ingredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
