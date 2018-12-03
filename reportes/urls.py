from django.contrib import admin
from django.urls import path
from reportes import views

urlpatterns = [
	
	path('index/', views.index, name='index_view'),
	path('', views.login_user, name='login_view'),
	path('logout', views.logout_user, name = 'logout_view'),
	path('busqueda/', views.buscador_etiquetas, name='buscador_etiquetas_view'),
	path('producto_indiv_list/', views.producto_indiv_list, name='producto_indiv_list_view'),
	path('lote_list/', views.lote_list, name='lote_list_view'),
	path('orden_almacen_list/', views.orden_almacen_list, name='orden_almacen_list_view'),
	path('piezas_indiv_list/', views.piezas_indiv_list, name='piezas_indiv_list_view'),

	# Detalles 
	path('detalle_producto_indiv/<int:id>', views.detalle_producto_indiv, name = 'detalle_producto_indiv_view'),
	path('detalle_lote/<int:id>', views.detalle_lote, name = 'detalle_lote_view'),
	path('detalle_orden_almacen/<int:id>', views.detalle_orden_almacen, name = 'detalle_orden_almacen_view'),

	# Pruebas y cosas locas 
	path('create_producto_indiv/', views.create_producto_indiv, name='create_producto_indiv_view'),

	# Formularios
	#path('registrar_productos_indiv/', views.registrar_productos_indiv.as_view(), name ='registrar_productos_indiv_views'),
	path('registrar_productos_gral/', views.registrar_productos_gral, name ='registrar_productos_gral_views'),
	path('registrar_lote/', views.registrar_lote, name ='registrar_lote_views'),
	path('registrar_linea/', views.registrar_linea, name ='registrar_linea_views'),
	path('registrar_area/', views.registrar_area, name ='registrar_area_views'),
	path('registrar_piezas_gral/', views.registrar_piezas_gral, name ='registrar_piezas_gral_views'),
	path('registrar_piezas_indiv/', views.registrar_piezas_indiv, name ='registrar_piezas_indiv_views'),
	path('registrar_jefe_linea/', views.registrar_jefe_linea, name ='registrar_jefe_linea_views'),
	path('registrar_jefe_area/', views.registrar_jefe_area, name ='registrar_jefe_area_views'),
	path('registrar_orden_almacen/', views.registrar_orden_almacen, name ='registrar_orden_almacen_views'),
]