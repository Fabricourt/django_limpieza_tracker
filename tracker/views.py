from django.shortcuts import render
from django_tables2 import RequestConfig
from tracker.models import opeDuquesa
from .tables import opeDuquesaTable
from django.views.generic import ListView
import datetime

# Create your views here.

def home(request):
	return render(request, "base.html")

def recoleccion_circ_2_3(request):
	start_date = datetime.date(2016, 9, 01)
	end_date = datetime.date(2016, 9, 10)
	query_results = opeDuquesa.objects.filter(date__range=(start_date, end_date))
	table = opeDuquesaTable(query_results)


	return render(request, "recoleccion_circ2_3.html", {'table': table})

