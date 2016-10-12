import django_tables2 as tables
from tracker.models import opeDuquesa

class opeDuquesaTable(tables.Table):
    class Meta:
        model = opeDuquesa
