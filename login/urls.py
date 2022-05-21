from django.urls import path
from . import views
app_name = "login"

urlpatterns = [
    path('', views.login, name='login'),
    path('log-out/', views.logout, name='logout'),
    path('sign-up/', views.signup, name='signup'),
]