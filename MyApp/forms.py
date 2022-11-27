
from django import forms
from MyApp.models import CookingRecipes

class RecipeModel2Form(forms.ModelForm):
    class Meta:
        model = CookingRecipes
        fields = '__all__'