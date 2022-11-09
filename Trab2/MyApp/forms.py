
from django import forms
from MyApp.models import Recipe

class RecipeModel2Form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'