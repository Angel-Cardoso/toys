from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Productos_indiv, Productos_gral, Areas, Lineas
from .models import Lotes, Piezas_gral, Piezas_indiv
from .models import Jefe_area, Jefe_linea, Orden_almacen
# Formas
from .forms import FormRegProductos_Indiv, FormRegProductos_gral, FormRegAreas, FormRegLineas
from .forms import FormRegJefe_linea, FormRegJefe_area, FormRegOrden_almacen, FormRegPiezas_indiv
from .forms import FormRegPiezas_gral, FormRegLote

# Create your views here.
@login_required(login_url = "/")
def index(request):
	return render(request,'reportes/index.html',{})

@login_required(login_url = "/")
def create_producto_indiv(request):
	if request.method == "POST":
		form = FormRegProductos_Indiv(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			if post.calificacion <= 20:
				post.prueba_estado = "rechazado"
			else:
				post.prueba_estado = "aprobado"
			post.prueba = post.etiqueta
			post.save()
			return redirect('detalle_producto_indiv_view', id =post.id)
	else:
		form = FormRegProductos_Indiv()
	return render(request, "reportes/registrar_productos_indiv.html", {'form': form})


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

def logout_user(request):
	context = {}
	if request.method == "POST":
		logout(request)
		return HttpResponseRedirect(reverse('login_view'))
	return render(request, "reportes/login.html", context)

# Detalles
@login_required(login_url = "/")
def detalle_orden_almacen(request, id=1):
	queryset = Orden_almacen.objects.get(id=id)
	return render(request, "reportes/detalle_orden_almacen.html", {"object" : queryset})

@login_required(login_url = "/")
def detalle_producto_indiv(request, id=1):
	queryset = Productos_indiv.objects.get(id=id)
	return render(request, "reportes/detalle_producto_indiv.html", {"object" : queryset})

@login_required(login_url = "/")
def buscador_etiquetas(request):
	q = request.GET.get('q','')
	querys = (Q(prueba__icontains=q))
	
	productos = Productos_indiv.objects.filter(querys)
	return render(request, "reportes/buscador_etiquetas.html",{ "object_list" : productos})


@login_required(login_url = "/")
def detalle_lote(request, id=1):
	queryset = Lotes.objects.get(id=id)
	return render(request, "reportes/detalle_lote.html", {"object" : queryset})

# Listas
@login_required(login_url = "/")
def orden_almacen_list(request):
	queryset = Orden_almacen.objects.all()
	return render(request, "reportes/orden_almacen_list.html",{ "object_list" : queryset})

@login_required(login_url = "/")
def producto_indiv_list(request):
	queryset = Productos_indiv.objects.all()
	return render(request, "reportes/productos_indiv.html",{ "object_list" : queryset})

	# template_name = "reportes/productos_indiv.html"
	# model = Productos_indiv

@login_required(login_url = "/")
def lote_list(request):
	queryset = Lotes.objects.all()
	return render(request, "reportes/lote_list.html",{ "object_list" : queryset})

@login_required(login_url = "/")
def piezas_indiv_list(request):
	queryset = Piezas_indiv.objects.all()
	return render(request, "reportes/piezas_indiv_list.html",{ "object_list" : queryset})


# Formas
@login_required(login_url = "/")
def registrar_lote(request):
	if request.method == "POST":
		form = FormRegLote(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('detalle_lote_view', id =post.id)
	else:	
		form = FormRegLote()
	return render(request, "reportes/registrar_lote.html", {'form': form})

@login_required(login_url = "/")
def registrar_productos_gral(request):
	if request.method == "POST":
		form = FormRegProductos_gral(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegProductos_gral()
	return render(request, "reportes/registrar_productos_gral.html", {'form': form})

@login_required(login_url = "/")
def registrar_area(request):
	if request.method == "POST":
		form = FormRegAreas(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegAreas()
	return render(request, "reportes/registrar_area.html", {'form': form})

@login_required(login_url = "/")
def registrar_linea(request):
	if request.method == "POST":
		form = FormRegLineas(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegLineas()
	return render(request, "reportes/registrar_linea.html", {'form': form})

@login_required(login_url = "/")
def registrar_piezas_gral(request):
	if request.method == "POST":
		form = FormRegPiezas_gral(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegPiezas_gral()
	return render(request, "reportes/registrar_pieza_gral.html", {'form': form})

@login_required(login_url = "/")
def registrar_piezas_indiv(request):
	if request.method == "POST":
		form = FormRegPiezas_indiv(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegPiezas_indiv()
	return render(request, "reportes/registrar_pieza_indiv.html", {'form': form})

@login_required(login_url = "/")
def registrar_jefe_linea(request):
	if request.method == "POST":
		form = FormRegJefe_linea(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegJefe_linea()
	return render(request, "reportes/registrar_jefe_linea.html", {'form': form})

@login_required(login_url = "/")
def registrar_jefe_area(request):
	if request.method == "POST":
		form = FormRegJefe_area(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegJefe_area()
	return render(request, "reportes/registrar_jefe_area.html", {'form': form})

@login_required(login_url = "/")
def registrar_orden_almacen(request):
	if request.method == "POST":
		form = FormRegOrden_almacen(request.POST)
		if form.is_valid():
			post = form.save(commit =True)
			post.save()
			return redirect('index_view')
	else:
		form = FormRegOrden_almacen()
	return render(request, "reportes/registrar_orden_almacen.html", {'form': form})