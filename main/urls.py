from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.main, name='main'),
    path('home', views.logout, name='logout'),
]