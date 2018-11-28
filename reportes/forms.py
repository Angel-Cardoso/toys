from django import forms
from .models import Productos_indiv


class FormRegProductos_Indiv(forms.ModelForm):
	class Meta:
		model = Productos_indiv
		fields = ["nombre_producto", "linea", "resistencia", "presentacion",
		"tamaño", "movilidad", "empaque", "fabrica", "piezas"]