
from django.urls.conf import path
from MyApp import views

app_name = "MyApp"

urlpatterns = [
path('list/', views.RecipeListView.as_view(),
    name='lista-recipes'),
path('', views.RecipeListView.as_view(),
    name='home-recipes'),
]