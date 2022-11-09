from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Recipe
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from MyApp.forms import RecipeModel2Form

# Create your views here.

def home(request):
# processamento antes de mostrar a home page
    return render(request, 'MyApp/home.html')

class RecipeListView(View):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        contexto = {'recipes': recipes, }
        return render(
            request,
            'MyApp/listRecipes.html',
            contexto)

class RecipeCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'form': RecipeModel2Form, }
        return render(request, "MyApp/createRecipe.html", contexto)
    
    def post(self, request, *args, **kwargs):
        form = RecipeModel2Form(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
        return HttpResponseRedirect(reverse_lazy(
            "MyApp:list-recipes"))