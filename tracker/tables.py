import django_tables2 as tables
from tracker.models import opeDuquesa



class opeDuquesaTable(tables.Table):
	camion = tables.Column()
	ton = tables.Column()
	date = tables.Column(order_by=('date'))

	class Meta:
		model = opeDuquesa
		fields = ('camion','ton')
		row_attrs = {
            'date': lambda record: record.pk
        }
		attrs = {'class': 'bordered centered'}


#table = opeDuquesa(opeDuquesa)
