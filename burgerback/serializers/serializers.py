from rest_framework import serializers
from burgerback.models import Ingredient
from django.contrib.auth.models import User


class IngredientSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'price', 'ordered', 'user']

    def create(self, validated_data):
        user = Ingredient.objects.only('id').get(id=validated_data['user'])
        return Ingredient.objects.create(**validated_data, user=user)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.ordered = validated_data.get('ordered', instance.ordered)
        instance.user = validated_data.get('ordered', instance.ordered)
        instance.save()
        return instance


class CreateUserSerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredient.objects.all())
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password((validated_data['password']))
        user.save()
        return user
