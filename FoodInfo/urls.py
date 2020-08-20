from django.urls import path
from . import views

app_name = 'FoodInfo'

urlpatterns = [
    path('service/', views.service, name='service'),
    path('search/', views.search, name='search'),
    path('addTodayFood/', views.addTodayFood, name='addTodayFood'),
]