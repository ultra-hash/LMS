from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('create/', views.create, name="books.create"),
    path('list/', views.list, name="books.list"),
    path('update/<pk>', views.update, name="books.update"),
    path('delete/<pk>', views.delete, name="books.delete"),
]
