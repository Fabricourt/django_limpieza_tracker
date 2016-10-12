from django.shortcuts import render
from django_tables2 import RequestConfig
from tracker.models import opeDuquesa
from .tables import opeDuquesaTable

# Create your views here.

def home(request):
	return render(request, "base.html")

def recoleccion_circ_2_3(request):
	query_results = opeDuquesa.objects.all()
	table = opeDuquesaTable(query_results)
	return render(request, "recoleccion_circ2_3.html", {'table': table})
