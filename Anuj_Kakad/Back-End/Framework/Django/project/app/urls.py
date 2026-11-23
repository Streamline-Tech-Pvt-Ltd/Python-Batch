from django.urls import path
from . import views

urlpatterns = [
    path('Display_Message/', views.display_message),
    path("Home/", views.home),
]