from django.shortcuts import render
from django.http import HttpResponse

from .models import FarmAnimal

# Create your views here.

def hello_world(request):
	text = "<h1>EXITOOO</h1>"
	return HttpResponse(text)

def index(request):
	farmAnimals = FarmAnimal.objects.all()
	text = ', '.join([f.animal_name for f in farmAnimals])
	return HttpResponse(text)
