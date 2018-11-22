from django.contrib import admin
from django.urls import path
from reportes import views

urlpatterns = [
	
	path('', views.index, name='index_view'),
]