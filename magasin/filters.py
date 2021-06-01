import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CommandFilter(django_filters.FilterSet):

	class Meta:
		model = Commande
		fields = '__all__'
class OrderFilter(django_filters.FilterSet):

	class Meta:
		model = Order
		fields = '__all__'