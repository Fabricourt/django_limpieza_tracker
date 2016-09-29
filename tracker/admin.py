from django.contrib import admin

from import_export.admin import ImportExportMixin, ExportActionModelAdmin 
from tracker.models import opeDuquesa

# Register your models here.

class opeDuquesaAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['date']


admin.site.register(opeDuquesa, opeDuquesaAdmin)