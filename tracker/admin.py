from django.contrib import admin
from import_export import resources

from import_export.admin import ImportExportMixin, ExportActionModelAdmin 
from tracker.models import opeDuquesa, Camion, Compania, Sectores, Circunscripcion, Supervisor

# Register your models here.

class CamionesResource(resources.ModelResource):

    class Meta:
         model = Camion
         import_id_fields=['ficha']

class SectoresResource(resources.ModelResource):

    class Meta:
         model = Sectores
         import_id_fields=['nombre','supervisor_area']


class opeDuquesaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date']

class CamionesAdmin(ImportExportMixin, admin.ModelAdmin):
	list_filter = ['ficha']
	resource_class = CamionesResource

class SectoresAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['nombre']
    resource_class = SectoresResource


admin.site.register(opeDuquesa, opeDuquesaAdmin)
admin.site.register(Camion, CamionesAdmin)
admin.site.register(Compania)
admin.site.register(Supervisor)
admin.site.register(Circunscripcion)
admin.site.register(Sectores, SectoresAdmin)