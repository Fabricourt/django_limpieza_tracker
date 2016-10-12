from django.contrib import admin
from import_export import resources

from import_export.admin import ImportExportMixin, ExportActionModelAdmin 
from tracker.models import opeDuquesa, Camion, Compania, Circunscripcion

# Register your models here.

class CamionesResource(resources.ModelResource):

    class Meta:
         model = Camion
         import_id_fields=['ficha']


class opeDuquesaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date']

class CamionesAdmin(ImportExportMixin, admin.ModelAdmin):
	list_filter = ['ficha']
	resource_class = CamionesResource


admin.site.register(opeDuquesa, opeDuquesaAdmin)
admin.site.register(Camion, CamionesAdmin)
admin.site.register(Compania)
admin.site.register(Circunscripcion)