from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Recipe
from django.views.generic.base import View

# Create your views here.

class RecipeListView(View):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        contexto = {'recipes': recipes, }
        return render(
            request,
            'MyApp/listRecipes.html',
            contexto)