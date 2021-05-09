from django.urls import path 

from . import views

urlpatterns = [
    path('', views.messages_index, name= 'messages_index'),
]