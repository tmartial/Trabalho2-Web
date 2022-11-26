
from django.urls.conf import path
from MyApp import views

app_name = "MyApp"

urlpatterns = [
path('atualize/<int:pk>/', views.RecipeUpdateView.as_view(),
    name='atualize-recipe'),
path('create/', views.RecipeCreateView.as_view(),
    name='create-recipe'),
path('list/', views.RecipeListView.as_view(),
    name='list-recipes'),
path('', views.home,
    name='home-recipes'),
]