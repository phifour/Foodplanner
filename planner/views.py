#from tkinter.tix import INTEGER
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe_Ingredient_Mapping, Recipe, Ingredient, Mealplan, RecipeFilter
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.template import loader

from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#import reportlab
import datetime
from .forms import FoodplanForm
import io
from django import forms
from random import randrange


def index(request):
    template = loader.get_template('planner/index.html')
    #user = request.user
    #users = User.objects.all()
    context = {}
    return HttpResponse(template.render(context, request))


def func_create_foodplan(request):
    Mealplan.objects.all().delete()
    #print('request',request.GET)
    #days = request.POST.get['timehorizon']
    user = request.user

    #submitbutton= request.POST.get("submit")
    form= FoodplanForm(request.POST or None)
    if form.is_valid():
        timehorizon= int(form.cleaned_data.get("timehorizoin"))
        cookingtime= int(form.cleaned_data.get("cooktime"))
        number_of_incredients_max= form.cleaned_data.get("number_of_incredients_max")
        vegetarian= form.cleaned_data.get("vegetarian")

        user = request.user
        found_recipies = Recipe.objects.filter(cooktime__lte=cookingtime)
        if vegetarian:
            found_recipies = found_recipies.exclude(incredientstext__icontains='Fleisch')
            found_recipies = found_recipies.exclude(incredientstext__icontains='speck')
            found_recipies = found_recipies.exclude(incredientstext__icontains='Hühnerbrust')
            found_recipies = found_recipies.exclude(incredientstext__icontains='Lamm')
            found_recipies = found_recipies.exclude(incredientstext__icontains='Kümmelbraten')
            found_recipies = found_recipies.exclude(incredientstext__icontains='Schinken')

    

        for i in range(1,timehorizon+1):
            meal_date = datetime.datetime(2022, 1, i)
            rand_index = randrange(len(found_recipies))
            Mealplan.objects.create(recipe=found_recipies[rand_index],created_by_user = user,date=meal_date,day_number=i)

    #timehorizon = int(request.POST['timehorizoin'])
    #cookingtime = int(request.POST['cooktime'])
    #type = request.POST['type']
    #portions = request.POST['portions']
    #print(days,cookingtime,type,portions)
    #user = request.user
    #recipes = Recipe.objects.all()
    #print('Found recipies:',len(found_recipies))



    return redirect('todos:foodplaner')



def aggregate_incredients(mealplan):
    
    ingredients_total = []
    amap = {}
    measures = {}

    for meal in mealplan:
        #print(meal)
        #my_food_plan_x.append(Recipe.objects.filter(id=meal.recipe.id))#[0]
        recipe_ingredient_mapping = Recipe_Ingredient_Mapping.objects.filter(recipe=meal.recipe.id)
        
        for x in recipe_ingredient_mapping:
            #print('x',x, x.incredient.name)
            #ingredients_total.append(x)
            measures[x.incredient.name] = x.measure

            if x.incredient.name in amap:
                amap[x.incredient.name] = amap[x.incredient.name] + x.quantity
            else: 
                amap[x.incredient.name] = x.quantity
            
    for key in amap:
        obj = {'incredient':key,'quantity':amap[key],'type':measures[key]}
        ingredients_total.append(obj)
    
    return ingredients_total


def foodplaner(request):
    #create_foodplan(request)
    recipes = Recipe.objects.all()
    template = loader.get_template('planner/foodplaner.html')
    mealplan = Mealplan.objects.all()
    ingredients_total = aggregate_incredients(mealplan)
    context = {
        'recipes_list': recipes,
        'my_food_plan':mealplan,
        'ingredients_total_list':ingredients_total,
    }

    return HttpResponse(template.render(context, request))


def shoppingcart(request):
       #create_foodplan(request)
    recipes = Recipe.objects.all()
    template = loader.get_template('planner/shoppingcart.html')
    mealplan = Mealplan.objects.all()
    ingredients_total = aggregate_incredients(mealplan)
    # mytodos = Todo.objects
    # users = User.objects.all()
    context = {
        'recipes_list': recipes,
        'my_food_plan':mealplan,
        'ingredients_total_list':ingredients_total,
    }
    return HttpResponse(template.render(context, request))

def showrecipie(request,recipie_id):
    this_recipie = Recipe.objects.filter(id=recipie_id)
    #ingredients_total = aggregate_incredients([this_recipie[0]])
    recipe_ingredient_mapping = Recipe_Ingredient_Mapping.objects.filter(recipe=recipie_id)
    
    ingredients_total = []
    amap = {}
    measures = {}

    for x in recipe_ingredient_mapping:
            #print('x',x, x.incredient.name)
            #ingredients_total.append(x)
        measures[x.incredient.name] = x.measure

        if x.incredient.name in amap:
            amap[x.incredient.name] = amap[x.incredient.name] + x.quantity
        else: 
            amap[x.incredient.name] = x.quantity
            
    for key in amap:
        obj = {'incredient':key,'quantity':amap[key],'type':measures[key]}
        ingredients_total.append(obj)


    template = loader.get_template('planner/recipie.html')
    context = {
        'recipie': this_recipie[0],
        'ingredients_total_list':ingredients_total
    }

    return HttpResponse(template.render(context, request))



def findrecipe(request):

    search = request.GET.get('search')
    print('search',search)

    salz = Ingredient.objects.filter(name='Salz')

    if search==None:
        this_incredient = Ingredient.objects.filter(name='Salz')
    else:
        this_incredient = Ingredient.objects.filter(id=search)
    all_incredient = Ingredient.objects.all()
    #print(this_incredient[0])
    recipe_ingredient_mapping = Recipe_Ingredient_Mapping.objects.filter(incredient=this_incredient[0])
    #ingredients_total = aggregate_incredients([this_recipie[0]])
    alist = []

    for x in recipe_ingredient_mapping:
        alist.append(x.recipe.id)

    #found_recipies = Recipe.objects.filter(id__in=alist)
    found_recipies = Recipe.objects.filter(cook_time__lte=20)
    print('search', search)
    #incredient_xxx = request
    #print(incredient_xxx)
    #ype = request.POST['type']
    tt = 'Honig'
    template = loader.get_template('planner/findrecipe.html')

    context = {
        'incredient_list':all_incredient,
        'recipies': found_recipies,
        'search_field':this_incredient[0]
    }

    return HttpResponse(template.render(context, request))


from .forms import RecipieSearchForm

def recipie_filter(request):

    cooktime = request.GET.get('cooktime')
    nosalt = request.GET.get('nosalt')
    nosugar = request.GET.get('nosugar')


    if cooktime is None:
        cooktime = 30

    incredientstext = request.GET.get('incredientstext')

    #print('cook time',cook_time)
    #recipies_less_than_cooktime = Recipe.objects.filter(cook_time__gt=32)
    #recipies_less_than_cooktime = Recipe.objects.raw('SELECT * FROM todos_recipie WHERE cook_time == 30 ')

    #todos = Todo.objects.raw('SELECT * FROM todos_todo')

    number_of_incredients_max= request.GET.get('number_of_incredients_max')


    recipename = request.GET.get('recipename')


    dosnotcontain = request.GET.get('dosnotcontain')
    #f = RecipeFilter(request.GET, queryset=Recipe.objects.all())

    #f = RecipeFilter(request.GET, queryset=Recipe.objects.all())
    print('cooktime',cooktime,incredientstext,'nosalt',nosalt)

    queryset = Recipe.objects.all().filter(cooktime__lte=cooktime)

    if nosalt == 'on':
        queryset = queryset.exclude(incredientstext__icontains='Salz')

    if nosugar == 'on':
        queryset = queryset.exclude(incredientstext__icontains='Zucker')


    #if dosnotcontain != 'None':
    #    queryset = queryset.exclude(incredientstext__icontains=dosnotcontain)

    f = RecipeFilter({'cooktime_max': cooktime, 'incredientstext':incredientstext,'number_of_incredients_max':number_of_incredients_max}, queryset=queryset)



    print('recipename',recipename)

    if recipename is not None:
        print('------------------xxxxxx----------')
        queryset = Recipe.objects.all().filter(name__icontains=recipename)




    paginator = Paginator(queryset, 100)


    #f = RecipeFilter({'cooktime_max': cooktime, 'incredientstext':incredientstext,'number_of_incredients_max':number_of_incredients_max}, queryset=Recipe.objects.all())

    #f = RecipeFilter({'cooktime_max': 100, 'preparation':'','number_of_incredients_max':'5'}, queryset=Recipe.objects.all())


    #f = RecipeFilter(request.GET, queryset=recipies_less_than_cooktime)


    page = request.GET.get('page')
    #print(page)
    
    page_obj = paginator.get_page(page)

    #print('page_obj',page_obj)

    form = RecipieSearchForm(initial={'cooktime': cooktime,'nosalt':nosalt,'nosugar':nosugar})

    
    return render(request, 'planner/filtertemplate.html', 
    {'filter': f,
    'cooktime':cooktime,
    'nosalt':nosalt,
    'nosugar':nosugar,
    'number_of_incredients_max':number_of_incredients_max,
    'dosnotcontain':dosnotcontain,
    'page_obj': page_obj,
    'form': form    
    })


def createfoodplan(request):
    #create_foodplan(request)
    recipes = Recipe.objects.all()
    template = loader.get_template('planner/createfoodplan.html')
    mealplan = Mealplan.objects.all()
    form = FoodplanForm()
    
    ingredients_total = aggregate_incredients(mealplan)
    

    # mytodos = Todo.objects
    # users = User.objects.all()
    context = {
        'recipes_list': recipes,
        'my_food_plan':mealplan,
        'ingredients_total_list':ingredients_total,
        'form':form
    }

    return HttpResponse(template.render(context, request))



def addrecipetomealplan(request):
    recipe_id = request.POST['recipe']
    day = request.POST['day']
    #name = request.POST['name']
    recipe = Recipe.objects.filter(id=recipe_id)
    created_by_user = request.user
    name = 'apfel'
    Mealplan.objects.create(name=name,recipe=recipe[0],created_by_user = created_by_user,day_number=4)
    return redirect('planner:foodplaner')



def updaterecipefrommealplan(request, mealplan_id):
    mealplan = get_object_or_404(Mealplan, pk=mealplan_id)
    #mealplan.day_number = 42    
    recipe_id = request.POST['recipe']
    recipe = Recipe.objects.filter(id=recipe_id)
    mealplan.recipe = recipe[0]
    mealplan.save()
    return redirect('planner:foodplaner')

def removerecipefrommealplan(request, mealplan_id):
    mealplan = get_object_or_404(Mealplan, pk=mealplan_id)
    mealplan.delete()
    return redirect('planner:foodplaner')



@login_required
def secret(request):
  
    template = loader.get_template('planner/secret.html')

    context = {
        'data': [1,2,3,4],
    }
    return HttpResponse(template.render(context, request))



def test(request):
    return HttpResponse("Hello, World!")