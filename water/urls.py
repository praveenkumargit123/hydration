from django.urls import path
from .import views

urlpatterns = [ 
        path('', views.home, name='home'), 
        path('remainder/',views.remainder,name='remainder'),]