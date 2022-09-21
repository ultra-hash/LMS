from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('create/', views.create, name="books.create"),
]
