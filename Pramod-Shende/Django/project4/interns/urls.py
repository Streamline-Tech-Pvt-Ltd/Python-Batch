from django.urls import path
from . import views
urlpatterns = [
    path('',views.intern_list, name='intern_list'),
    
]