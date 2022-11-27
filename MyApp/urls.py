
from django.urls.conf import path
from MyApp import views
from django.urls.base import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordChangeDoneView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

app_name = "MyApp"

urlpatterns = [
path('remove/<int:pk>/', views.RecipeDeleteView.as_view(),
    name='remove-recipe'),
path('atualize/<int:pk>/', views.RecipeUpdateView.as_view(),
    name='atualize-recipe'),
path('create/', views.RecipeCreateView.as_view(),
    name='create-recipe'),
path('accounts/profile/', views.RecipeListView.as_view(),
    name='list-recipes'),
path('accounts/', views.controlView,
    name='control-recipe'),
path('accounts/registro/',views.register,
    name='register-recipe'),
path('accounts/login/',LoginView.as_view(template_name='MyApp/login.html',),
    name='login-recipe'),
path('accounts/logout/',LogoutView.as_view(next_page=reverse_lazy('MyApp:login-recipe'),),
    name='logout-recipe'),
path('accounts/password_change/',PasswordChangeView.as_view(template_name='MyApp/changePassword.html',
    success_url=reverse_lazy('MyApp:list-recipes'),),
     name='recipe-modification-PW'),
path('accounts/password_change_done/',PasswordChangeDoneView.as_view(template_name='MyApp/validationNewPW.html',), 
    name='recipe-validation-PW'),
path('accounts/terminaRegistro/<int:pk>/',
    UpdateView.as_view(template_name='MyApp/user_form.html',
    success_url=reverse_lazy('MyApp:list-recipes'),
    model=User,
    fields=[
        'first_name',
        'last_name',
        'email',
    ],
    ), name='recipe-DataUser'),
path('accounts/password_reset/', PasswordResetView.as_view(
    template_name='MyApp/password_reset_form.html',
    success_url=reverse_lazy('MyApp:sec-password_reset_done'),
    email_template_name='MyApp/password_reset_email.html',
    subject_template_name='MyApp/password_reset_subject.txt',
    from_email='thomas.martial@insa-lyon.fr',
    ), name='password_reset'),
path('accounts/password_reset_done/', 
    PasswordResetDoneView.as_view(template_name='MyApp/password_reset_done.html',
    ), name='sec-password_reset_done'),
path('accounts/password_reset_confirm/<uidb64>/<token>/',
    PasswordResetConfirmView.as_view(template_name='MyApp/password_reset_confirm.html',
    success_url=reverse_lazy('MyApp:sec-password_reset_complete'),
    ), name='password_reset_confirm'),
path('accounts/password_reset_complete/', 
    PasswordResetCompleteView.as_view(template_name='MyApp/password_reset_complete.html'
    ), name='sec-password_reset_complete'),
path('', views.base,
    name='base-recipes'),
path('home/', views.home,
    name='home-recipes'),
]