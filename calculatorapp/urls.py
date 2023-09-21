
from django.urls import path,include
# from calculator import views

from . import views

urlpatterns = [
    
    path('', views.greetings),
    path('calculation',views.calculation)
]