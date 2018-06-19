from django.http import Http404
from django.shortcuts import render
from .models import Drink
from django.views.generic.edit import CreateView

def index(request):
	all_drinks = Drink.objects.all()
	context = { 'all_drinks': all_drinks }
	return render(request, 'energy/index.html', context)

def detail(request, Drink_id):
	try:
		drink = Drink.objects.get(pk=Drink_id)
	except Drink.DoesNotExist:
		raise Http404("Drink does not exist")
	return render(request, 'energy/detail.html', {'drink': drink})
