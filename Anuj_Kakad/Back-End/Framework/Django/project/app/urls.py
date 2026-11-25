from django.urls import path
from . import views

urlpatterns = [
    path('Display/', views.display_message),
    path('home/', views.home),
    path('date/', views.date),
    path('calculator/', views.calculator),
    path('ifdemo/', views.ifdemo),
    path('fordemo/', views.fordemo),
    path('user_data/', views.user_Data),
]