from django.urls import path
from static_app import views
urlpatterns = [
    path('', views.home, name='home'),
        
]
