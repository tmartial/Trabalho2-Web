from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from MyApp.models import CookingRecipes
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from MyApp.forms import RecipeModel2Form
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
    return render(request, 'MyApp/homepage.html')

def base(request):
    return render(request, 'MyApp/base.html')

def controlView(request):
    return render(request,"MyApp/controlAccess.html")

class RecipeListView(View):
    def get(self, request, *args, **kwargs):
        recipes = CookingRecipes.objects.all()
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
        return HttpResponseRedirect(reverse_lazy("MyApp:list-recipes"))
        
class RecipeUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        recipes = CookingRecipes.objects.get(pk=pk)
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
        recipe = CookingRecipes.objects.get(pk=pk)
        context = {'recipe': recipe, }
        return render(request,'MyApp/deleteRecipe.html',context)

    def post(self, request, pk, *args, **kwargs):
        recipe = CookingRecipes.objects.get(pk=pk)
        recipe.delete()
        return HttpResponseRedirect(reverse_lazy("MyApp:list-recipes"))

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MyApp/control-recipe')
    else:
        form = UserCreationForm()
    context = {'form': form, }
    return render(request,'MyApp/register.html', context)

def secretPage(request):
    return render(request,'MyApp/listRecipes.html')

class MyUpdateView(UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, args, kwargs)
        else:
            return redirect('MyApp/control-recipe')