from django.shortcuts import render
from tracker.models import opeDuquesa

# Create your views here.

def home(request):
	return render(request, "base.html")

def recoleccion_circ_2_3(request):
	query_results = opeDuquesa.objects.all().values_list('date')
	return render(request, "recoleccion_circ2_3.html")
