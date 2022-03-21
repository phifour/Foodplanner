# myapi/urls.py
# todo/api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
#from .views import TodoListApiView
from .views import todo_list, list_users, incredient_list, recipie_list,recipie_add_incredient
from rest_framework.urlpatterns import format_suffix_patterns


# urlpatterns = [
#     path('', TodoListApiView.as_view()),
#     path('getlist', TodoListApiView.get)
# ]

urlpatterns = [
    path('list/', todo_list),
    path('list_users/', list_users),
    path('list_incredient/', incredient_list),
    path('list_recipie/', recipie_list),
    path('recipie_add_incredient/', recipie_add_incredient)    
]

urlpatterns = format_suffix_patterns(urlpatterns)
