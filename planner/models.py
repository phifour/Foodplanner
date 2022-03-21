from django.db import models
from django.conf import settings # new
from django.contrib.auth.models import User
import django_filters
from django_filters import RangeFilter

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140, unique=False, verbose_name="Name")
    link = models.CharField(max_length=120, unique=True, verbose_name="Link")
    image_link = models.CharField(max_length=300, unique=True, verbose_name="Image_Link")
    type = models.CharField(max_length=20,choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'),
                ('SOUP', 'Soup'),('DINNER', 'Dinner')])
    cooktime = models.IntegerField()
    number_of_incredients = models.IntegerField()
    preparation = models.TextField()
    incredientstext = models.CharField(max_length=500, unique=False, verbose_name="Incredients Text")
    #incredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    #thumbnail = models.ImageField(upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")
    #tags = TaggableManager()
    incredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

class Recipe_Ingredient_Mapping(models.Model):
    id = models.AutoField(primary_key=True)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='recipe')
    incredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name='incredient')
    created_at = models.DateTimeField('Created', auto_now_add=True)
    quantity = models.FloatField()
    
    measures_list = [( 'CM', 'cm' ),
    ( 'WF' ,'Wf' ),
    ( 'G' ,'g' ),
    ( 'SCHB' ,'Schb' ),
    ( 'EL' ,'EL' ),
    ( 'MSP' ,'Msp' ),
    ( 'BECHER' ,'Becher' ),
    ( 'TASSE' ,'Tasse' ),
    ( 'KN' ,'Kn' ),
    ( 'ML' ,'ml' ),
    ( 'KPF' ,'kpf' ),
    ( 'BUND' ,'Bund' ),
    ( 'PA' ,'Pa' ),
    ( 'ZWEIG' ,'Zweig' ),
    ( 'PK' , 'Pk' ),
    ( 'SPR' ,'Spr' ),
    ( 'KG' ,'kg' ),
    ( 'SCHUSS' ,'Schuss' ),
    ( 'DOSE' ,'Dose' ),
    ( 'CL' ,'cl' ),
    ( 'SP' ,'Sp' ),
    ( 'STK' ,'Stk' ),
    ( 'TL' ,'TL' ),
    ( 'L' ,'l' ),
    ( 'TR' ,'Tr' ),
    ( 'MG' ,'mg' ),
    ( 'STG' ,'Stg' ),
    ( 'PRISE' ,'Prise' ),
    ( 'KUGEL' ,'Kugel' ),
    ( 'BL' ,'Bl' )]

    #type = models.CharField(max_length=20,choices=[('NUMBER', 'Number'), ('GRAMM', 'Gramm'), ('KILO', 'Klio')])

    measure = models.CharField(max_length=20,choices=measures_list)

    def __str__(self):
        return str(self.recipe) + ', // : ' + str(self.incredient)


class RecipeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')#iexact
    incredientstext = django_filters.CharFilter(lookup_expr='icontains')#iexact
    cooktime = RangeFilter()
    number_of_incredients = RangeFilter()

    class Meta:
        model = Recipe
        fields= ['name','cooktime','incredientstext','number_of_incredients']
        #fields = {'name':['contains'], 'cook_time':['lt']}



class Mealplan(models.Model):
    id = models.AutoField(primary_key=True)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,related_name='mealplan_recipe')
    day_number = models.IntegerField()
    date = models.DateTimeField('Date', auto_now_add=False)

    #thumbnail = models.ImageField(upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")

    def __str__(self):
        return str(self.recipe) + ' / ' + str(self.date)
