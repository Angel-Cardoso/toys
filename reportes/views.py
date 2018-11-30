from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Productos_indiv, Productos_gral, Areas, Lineas
from .models import Lotes, Piezas_gral, Piezas_indiv
from .models import Jefe_area, Jefe_linea, Orden_almacen
# Formas
from .forms import FormRegProductos_Indiv, FormRegProductos_gral, FormRegAreas, FormRegLineas
from .forms import FormRegJefe_linea, FormRegJefe_area, FormRegOrden_almacen

# Create your views here.
def index(request):
	return render(request,'reportes/index.html',{})

def login_user(request):
	context = {}
	if request.method == "POST":
		username = request.POST['usu']
		password = request.POST['con']
		user = authenticate(request, username=username,password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse('index_view'))
		else:
			context["error"] = "Credenciales desconocidas"
			return render(request,"reportes/login.html", context)
	else: 
		return render(request,"reportes/login.html", context)

# Detalles
class detalle_orden_almacen(generic.DetailView):
 	template_name = "reportes/detalle_orden_almacen.html"
 	model = Orden_almacen

class detalle_producto_indiv(generic.DetailView):
 	template_name = "reportes/detalle_producto_indiv.html"
 	model = Productos_indiv

class buscador_etiquetas(generic.ListView):
	template_name = "reportes/buscador_etiquetas.html"
	queryset = Productos_indiv.objects.all()

	def get_queryset(self, *args, **kwargs):
	 	qs = Productos_indiv.objects.all()
	 	print(self.request.GET)
	 	query = self.request.GET.get("q",None)
	 	if query is not None:
	 		qs = qs.filter(Q(fabrica__icontains=query) | Q(nombre_producto__nombre_producto__icontains=query))
	 	return qs

class detalle_lote(generic.DetailView):
 	template_name = "reportes/detalle_lote.html"
 	model = Lotes

# Listas
class orden_almacen_list(generic.ListView):
	template_name = "reportes/orden_almacen_list.html"
	model = Orden_almacen

class producto_indiv_list(generic.ListView):
	template_name = "reportes/productos_indiv.html"
	model = Productos_indiv

class lote_list(generic.ListView):
	template_name = "reportes/lote_list.html"
	model = Lotes

class piezas_indiv_list(generic.ListView):
	template_name = "reportes/piezas_indiv_list.html"
	model = Piezas_indiv

# Formas

class registrar_productos_indiv(generic.CreateView):
	template_name = "reportes/registrar_productos_indiv.html"
	model = Productos_indiv
	fields = ["nombre_producto", "linea", "resistencia", "presentacion",
		"tamaño", "movilidad", "empaque", "fabrica", "piezas"]
	success_url = "/index/"

class registrar_productos_gral(generic.CreateView):
	template_name = "reportes/registrar_productos_gral.html"
	model = Productos_gral
	fields = ["nombre_producto", "precio"]
	success_url = "/index/"

class registrar_area(generic.CreateView):
	template_name = "reportes/registrar_area.html"
	model = Areas
	fields = ["nombre_area"]
	success_url = "/index/"

class registrar_linea(generic.CreateView):
	template_name = "reportes/registrar_linea.html"
	model = Lineas
	fields = ["area"]
	success_url = "/index/"

class registrar_piezas_gral(generic.CreateView):
	template_name = "reportes/registrar_pieza_gral.html"
	model = Piezas_gral
	fields = ["nombre_pieza", "proveedor", "precio"]
	success_url = "/index/"

class registrar_piezas_indiv(generic.CreateView):
	template_name = "reportes/registrar_pieza_indiv.html"
	model = Piezas_indiv
	fields = ["nombre_pieza"]
	success_url = "/index/"

class registrar_jefe_linea(generic.CreateView):
	template_name = "reportes/registrar_jefe_linea.html"
	model = Jefe_linea
	fields = ["user", "linea"]
	success_url = "/index/"

class registrar_jefe_area(generic.CreateView):
	template_name = "reportes/registrar_jefe_area.html"
	model = Jefe_area
	fields = ["user", "area"]
	success_url = "/index/"

class registrar_orden_almacen(generic.CreateView):
	template_name = "reportes/registrar_orden_almacen.html"
	model = Orden_almacen
	fields = ["user", "jefe_linea", "estado", "piezas"]
	success_url = "/index/"