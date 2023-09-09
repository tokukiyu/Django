from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('try/', views.TryMe, name='TryMe')
]