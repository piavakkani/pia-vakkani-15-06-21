from django.contrib import admin
from django.urls import path, include
from scraper import views

urlpatterns = [ 
    path('',views.list_view, name="list_view"),

]