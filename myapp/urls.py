from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('projects/', views.anotherFunction, name='test'),
    path('register/', views.register, name='register'),
    path('product/<comida>', views.producto, name='comida'),
]