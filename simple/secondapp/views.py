from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hola_chao(request):
	text = "<h1>HOLIIII</h1>"
	return HttpResponse(text)
