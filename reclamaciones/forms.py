from django import forms
from reclamaciones.models import Reclamacion


class ReclamacionForm(forms.ModelForm):
   
    class Meta:
        model = Reclamacion
        fields = ('fecha_apertura', 'nombre', 'direccion', 'sector', 'telefono', 'tipo_reclamacion'
        	, 'observaciones', 'fecha_cierre', 'status')