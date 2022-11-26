from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from MyApp.models import Recipe
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from MyApp.forms import RecipeModel2Form

# Create your views here.

def home(request):
    return render(request, 'MyApp/home.html')

class RecipeListView(View):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        context = {'recipes': recipes, }
        return render(
            request,
            'MyApp/listRecipes.html',
            context)

class RecipeCreateView(View):
    def get(self, request, *args, **kwargs):
        context = { 'form': RecipeModel2Form, }
        return render(request, "MyApp/createRecipe.html", context)
    
    def post(self, request, *args, **kwargs):
        form = RecipeModel2Form(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
        return render(request, "MyApp/listRecipes.html",{
            'form': RecipeModel2Form()})
        


class RecipeUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        recipes = Recipe.objects.get(pk=pk)
        form = RecipeModel2Form(instance=recipes)
        context = {'recipes': recipes, }
        return render(request,'MyApp/actualizeRecipe.html', context)

    def post(self, request, pk, *args, **kwargs):
        recipes = get_object_or_404(Recipe, pk=pk)
        form = RecipeModel2Form(request.POST, instance=recipes)
        if form.is_valid():
            recipe = form.save() 
            recipe.save() 
            return HttpResponseRedirect(reverse_lazy("MyApp:list-recipes"))
        else:
            context = {'recipes': form, }
            return render(request,'MyApp/actualizeRecipe.html', context)

class RecipeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        recipe = Recipe.objects.get(pk=pk)
        context = {'recipe': recipe, }
        return render(request,'MyApp/deleteRecipe.html',context)

    def post(self, request, pk, *args, **kwargs):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return HttpResponseRedirect(reverse_lazy("MyApp:list-recipes"))
