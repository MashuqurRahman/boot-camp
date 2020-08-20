from django.contrib import admin
from django.urls import path,include
from .views import article

urlpatterns = [
    
    path('articles/',article.as_view(),name="article_list")
]

