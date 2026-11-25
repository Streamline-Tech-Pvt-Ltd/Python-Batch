from django.urls import path
from . import views

urlpatterns = [
    path('Display/', views.display_message),
    path('home/', views.home),
    path('date/', views.date),
]