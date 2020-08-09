from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [

    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('search', views.search, name='search'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),#when we enter the url with astring value as slug then it nmove to views with the string and rnder the texr inside the views with the string
    path('contact', views.contact, name='contact')



]