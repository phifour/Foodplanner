# todo/api/serializers.py
from rest_framework import serializers
from planner.models import Ingredient, Recipe,Recipe_Ingredient_Mapping
from django.contrib.auth.models import User
#from taggit.serializers import (TagListSerializerField,TaggitSerializer)

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name','id')

class RecipeSerializer(serializers.ModelSerializer):
    #tags = TagListSerializerField()
    #tag = TaggitSerializer(read_only=True, many=True).data

    class Meta:
        model = Recipe
        fields = ('name','type','id','link','image_link','cooktime','number_of_incredients','preparation','incredientstext')


class Recipe_Ingredient_MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe_Ingredient_Mapping
        fields = ('recipe','incredient','quantity','measure','created_by_user')
