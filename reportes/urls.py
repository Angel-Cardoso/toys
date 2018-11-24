from django.contrib import admin
from django.urls import path
from reportes import views

urlpatterns = [
	
	path('', views.index, name='index_view'),
	path('detalle_producto_indiv/<int:pk>', views.detalle_producto_indiv.as_view(), name = 'detalle_producto_indiv_view'),
]