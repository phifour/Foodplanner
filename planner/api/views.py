# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from planner.models import Ingredient, Recipe
from .serializers import CurrentUserSerializer, IngredientSerializer, RecipeSerializer
from .serializers import Recipe_Ingredient_Mapping, Recipe_Ingredient_MappingSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# class TodoListApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the todo items for given requested user
#         '''
#         todos = Todo.objects.filter(user = request.user.id)
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Todo with given todo data
#         '''
#         data = {
#             'title': request.data.get('title'), 
#             #'completed': request.data.get('completed'), 
#             'user': 1#request.user.id
#         }
#         serializer = TodoSerializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# def snippet_list(request):

@api_view(['GET', 'POST'])
def todo_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Todo.objects.all()
        serializer = TodoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def incredient_list(request, format = None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Ingredient.objects.all()
        serializer = IngredientSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def recipie_list(request, format = None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Recipe.objects.all()
        serializer = RecipeSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def recipie_add_incredient(request, format = None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Recipe_Ingredient_Mapping.objects.all()
        serializer = Recipe_Ingredient_MappingSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #request.data['quantity'] = ['99']
        serializer = Recipe_Ingredient_MappingSerializer(data=request.data)
        recipe_id = request.POST['recipe']
        print('request.data',request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # day = request.POST['day']
    # #name = request.POST['name']
    # recipe = Recipe.objects.filter(id=recipe_id)
    # created_by_user = request.user
    # name = 'apfel'
    # Mealplan.objects.create(name=name,recipe=recipe[0],created_by_user = created_by_user,day_number=4)




@api_view(['GET', 'POST'])
def list_users(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    #User = get_user_model()
    #users = User.objects.all()
    if request.method == 'GET':
        users = User.objects.all()
        serializer = CurrentUserSerializer(users, many=True)
        return Response(serializer.data)







# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)