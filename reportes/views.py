from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Productos_indiv,Usuario
from .models import Lotes

# Formas
from .forms import FormRegProductos_Indiv


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
	success_url = "/index/"

