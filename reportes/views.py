from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from .models import Productos_indiv,Usuario
from .models import Lotes

# Formas
from .forms import FormRegProductos_Indiv


# Create your views here.
def index(request):
	try:
		if request.method == 'POST':
			usu = request.POST.get('usu')
			con = request.POST.get('con')

			usuario = Usuario.objects.get(usuario=usu,contrasena=con)

			request.session['usuario']=usu
		return render(request, "reportes/index.html",{})
	except:
		return render(request,'reportes/login.html',{})

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
		"tamaño", "movilidad", "empaque", "fabrica", "piezas"]
	success_url = "/"

def login(request):
	return render(request,'reportes/login.html',{})
