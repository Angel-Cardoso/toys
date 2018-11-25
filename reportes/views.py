from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from .models import Productos_indiv
from .models import Lotes

# Formas
from .forms import FormRegProductos_Indiv


# Create your views here.
def index(request):
	return render(request, "reportes/index.html")

class detalle_producto_indiv(generic.DetailView):
 	template_name = "reportes/detalle_producto_indiv.html"
 	model = Productos_indiv

class detalle_lote(generic.DetailView):
 	template_name = "reportes/detalle_lote.html"
 	model = Lotes

# Formas

class registrar_productos_indiv(generic.CreateView):
	template_name = "reportes/registrar_productos_indiv.html"
	model = Productos_indiv
	fields = ["nombre_producto", "linea", "resistencia", "presentacion",
		"tamaño", "movilidad", "empaque", "fabrica"]
	success_url = "/"
