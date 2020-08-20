from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Article

# Create your views here.
class article(ListView):
    model = Article
    template_name='article_app/articles.html'
    