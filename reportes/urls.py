from django.contrib import admin
from django.urls import path
from reportes import views

urlpatterns = [
	
	path('index/', views.index, name='index_view'),
	path('', views.login_user, name='login_view'),
	path('busqueda/', views.buscador_etiquetas.as_view(), name='buscador_etiquetas_view'),
	path('producto_indiv_list/', views.producto_indiv_list.as_view(), name='producto_indiv_list_view'),
	path('lote_list/', views.lote_list.as_view(), name='lote_list_view'),
	path('orden_almacen_list/', views.orden_almacen_list.as_view(), name='orden_almacen_list_view'),
	path('piezas_indiv_list/', views.piezas_indiv_list.as_view(), name='piezas_indiv_list_view'),

	# Detalles 
	path('detalle_producto_indiv/<int:pk>', views.detalle_producto_indiv.as_view(), name = 'detalle_producto_indiv_view'),
	path('detalle_lote/<int:pk>', views.detalle_lote.as_view(), name = 'detalle_lote_view'),
	path('detalle_orden_almacen/<int:pk>', views.detalle_orden_almacen.as_view(), name = 'detalle_orden_almacen_view'),


	# Formularios
	path('registrar_productos_indiv/', views.registrar_productos_indiv.as_view(), name ='registrar_productos_indiv_views'),
	path('registrar_productos_gral/', views.registrar_productos_gral.as_view(), name ='registrar_productos_gral_views'),
	path('registrar_linea/', views.registrar_linea.as_view(), name ='registrar_linea_views'),
	path('registrar_area/', views.registrar_area.as_view(), name ='registrar_area_views'),
	path('registrar_piezas_gral/', views.registrar_piezas_gral.as_view(), name ='registrar_piezas_gral_views'),
	path('registrar_piezas_indiv/', views.registrar_piezas_indiv.as_view(), name ='registrar_piezas_indiv_views'),
	path('registrar_jefe_linea/', views.registrar_jefe_linea.as_view(), name ='registrar_jefe_linea_views'),
	path('registrar_jefe_area/', views.registrar_jefe_area.as_view(), name ='registrar_jefe_area_views'),
	path('registrar_orden_almacen/', views.registrar_orden_almacen.as_view(), name ='registrar_orden_almacen_views'),
]