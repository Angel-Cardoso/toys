from django.contrib import admin
from django.urls import path
from reportes import views

urlpatterns = [
	
	path('', views.index, name='index_view'),
	
	# Detalles 
	path('detalle_producto_indiv/<int:pk>', views.detalle_producto_indiv.as_view(), name = 'detalle_producto_indiv_view'),
	path('detalle_lote/<int:pk>', views.detalle_lote.as_view(), name = 'detalle_lote_view'),

	# Formularios
	path('registrar_productos_indiv/', views.registrar_productos_indiv.as_view(), name ='registrar_productos_indiv_views'),
]