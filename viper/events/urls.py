from django.urls import path


from .views import index, CoordinatorDashboard

app_name = 'events'
urlpatterns = [
    path('', index),
    path('coordinator-dashboard/', CoordinatorDashboard, name='coordinator-dashboard')
]