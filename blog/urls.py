from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index,name='index'),
    path('post/<int:id>/',views.post_list,name='post_list')

]