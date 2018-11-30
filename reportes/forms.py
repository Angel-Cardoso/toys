from django import forms
from .models import Productos_indiv, Productos_gral, Areas, Lineas
from .models import Piezas_gral, Piezas_indiv, Jefe_area, Jefe_linea, Orden_almacen


class FormRegProductos_Indiv(forms.ModelForm):
	class Meta:
		model = Productos_indiv
		fields = ["nombre_producto", "linea", "resistencia", "presentacion",
		"tamaño", "movilidad", "empaque", "fabrica", "piezas"]

class FormRegProductos_gral(forms.ModelForm):
	class Meta:
		model = Productos_gral
		fields = ["nombre_producto", "precio"]

class FormRegAreas(forms.ModelForm):
	class Meta:
		model = Areas
		fields = ["nombre_area"]

class FormRegLineas(forms.ModelForm):
	class Meta:
		model = Lineas
		fields = ["area"]

class FormRegPiezas_gral(forms.ModelForm):
	class Meta:
		model = Piezas_gral
		fields = ["nombre_pieza", "proveedor", "precio"]

class FormRegPiezas_indiv(forms.ModelForm):
	class Meta:
		model = Piezas_indiv
		fields = ["nombre_pieza"]

class FormRegJefe_linea(forms.ModelForm):
	class Meta:
		model = Jefe_linea
		fields = ["user", "linea"]

class FormRegJefe_area(forms.ModelForm):
	class Meta:
		model = Jefe_area
		fields = ["user", "area"]

class FormRegOrden_almacen(forms.ModelForm):
	class Meta:
		model = Orden_almacen
		fields = ["user", "jefe_linea", "estado", "piezas"]