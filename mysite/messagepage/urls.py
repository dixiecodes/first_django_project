from django.urls import path 

from . import views

urlpatterns = [
    path('', views.messagepage_index, name= 'messagepage_index'),
]