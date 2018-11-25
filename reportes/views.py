from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from .models import Productos_indiv
from .models import Lotes
# Create your views here.
def index(request):
	return render(request, "reportes/index.html")

class detalle_producto_indiv(generic.DetailView):
 	template_name = "reportes/detalle_producto_indiv.html"
 	model = Productos_indiv

class detalle_lote(generic.DetailView):
 	template_name = "reportes/detalle_lote.html"
 	model = Lotes
