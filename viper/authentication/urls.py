'''from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    #path('coordinator-login/', views.CoordinatorLogin, name='coordinator-login'),
    #path('sign-up/', views.register, name='signup'),
    #path('log-in/', views.login, name='login')'''

from django.urls import path
from .views import (
            home,
            login_view,
            logout_view,
            account_view,
            registration_view,
        )
        
        
urlpatterns  = [
    path('register/',registration_view, name="register" ),
    path('logout/',logout_view, name="logout" ),
    path('login/',login_view, name="login" ),
    path('home/',home, name="home" ),
    path('profile/',account_view, name="account" ),
]
