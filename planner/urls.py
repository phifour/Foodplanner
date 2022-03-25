from django.urls import path, include
from . import views

app_name = 'planner'
#http://127.0.0.1:8000/planner/foodplaner/

urlpatterns = [
    path('', views.index, name='index'),
    path('secret', views.secret, name='secret'),
    path('addrecipetomealplan/', views.addrecipetomealplan, name='addrecipetomealplan'),
    path('<int:mealplan_id>/removerecipefrommealplan/', views.removerecipefrommealplan, name='removerecipefrommealplan'),
    path('<int:mealplan_id>/updaterecipefrommealplan/', views.updaterecipefrommealplan, name='updaterecipefrommealplan'),
    #path('api/', include('planner.api.urls')),
    path('foodplaner/', views.foodplaner, name='foodplaner'),
    path('shoppingcart/', views.shoppingcart, name='shoppingcart'),
    path('createfoodplan/', views.createfoodplan, name='createfoodplan'),
    path('func_create_foodplan/', views.func_create_foodplan, name='func_create_foodplan'),
    path('<int:recipie_id>/showrecipie/', views.showrecipie, name='showrecipie'),
    path('findrecipe/', views.findrecipe, name='findrecipe'),
    path('recipefilter/', views.recipie_filter, name='recipie_filter'),
    path('test/', views.test, name='test'),
    path('api/', include('planner.api.urls')),

]