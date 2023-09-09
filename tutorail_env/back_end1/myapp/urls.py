from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),  
    # path('try/', views.TryMe, name='TryMe')
]