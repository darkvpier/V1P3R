from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign-up/', views.SignUp, name='signup'),
    path('login/', views.LogIn, name='login')
]
