from django.shortcuts import render
import requests as r

# Create your views here.
def index(request):
    template='noticias/noticias.html'
    return render(request,template)

def mostrar10(request):
	template = 'noticias/10mejores.html'
	result = r.get('http://localhost:9000')
	noticias = result.json()
	print (noticias)
	return render(request, template, noticias)