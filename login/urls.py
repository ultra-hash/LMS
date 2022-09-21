from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login.login"),
    path('register/', views.login, name="login.login"),
]
