from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login.login"),
    path('logout/', views.logout, name="login.logout"),
    path('register/', views.register, name="login.register"),
    path('', views.index, name="login.index")
]
