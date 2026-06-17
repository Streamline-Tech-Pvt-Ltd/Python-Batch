from django.urls import path
from app import views

urlpatterns = [
    path('exp/', views.example),
    path('date/', views.date),
    path('ifdemo/',views.ifdemo),
    path('fordemo/',views.fordemo),
    path('user_data/',views.user_data),
    path('userdata2/',views.user_data2),
    path('user3/',views.LoadUserDetails, name='hello'),
    
]