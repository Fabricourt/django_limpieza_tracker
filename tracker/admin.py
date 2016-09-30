from django.contrib import admin

from import_export.admin import ImportExportMixin, ExportActionModelAdmin 
from tracker.models import opeDuquesa, Camion, Compania

# Register your models here.

class opeDuquesaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date']

class CamionesAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['ficha']


admin.site.register(opeDuquesa, opeDuquesaAdmin)
admin.site.register(Camion, CamionesAdmin)
admin.site.register(Compania)