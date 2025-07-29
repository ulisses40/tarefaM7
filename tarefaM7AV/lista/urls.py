from django.contrib import admin
from django.urls import path, include
from . import views

app_lista = "lista"


urlpatterns = [
    path('',views.homepage,name='homepage'),

]
