import django_tables2 as tables
from tracker.models import opeDuquesa


class opeDuquesaTable(tables.Table):
	camion = tables.Column()
	date = tables.Column(order_by=('date'))
	
	class Meta:
		model = opeDuquesa
		attrs = {'class': 'bordered centered'}
