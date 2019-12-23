from django.shortcuts import render, redirect
from reclamaciones.forms import ReclamacionForm


# Create your views here.


def reclamacion_new_form(request):
	form = ReclamacionForm(request.POST or None)
	return render(request, 'reclamacion_form.html', {'form': form})