from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login.login"),
    path('register/', views.register, name="login.register"),
]
