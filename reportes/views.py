from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q

# Create your views here.
def index(request):
	return render(request, "reportes/index.html")

