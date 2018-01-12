from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from datetime import datetime
from django.core import serializers
import json
# Create your views here.

from api.models import News

def home(request):
    fecha = datetime.now().date()
    key = str(fecha.year) + str (fecha.month) + str (fecha.day)
    hit = cache.get(key)
    if (hit == None):
        data = News.objects.all().order_by('-numero_accessos')[:10]
        sedata = serializers.serialize('json',data)
        cache.set(key,sedata,60*60*24)
        return HttpResponse(sedata, content_type='application/json')
    else:
        d = json.loads(hit)
        for news in d:
            print(news['fields']['title'])
        return HttpResponse(hit, content_type='application/json')

def justdatabase(request):
    data = News.objects.all().order_by('-numero_accessos')[:10]
    sedata = serializers.serialize('json',data)
    return HttpResponse(sedata, content_type='application/json')

def sendNews():
    fecha = datetime.now().date()
    key = str(fecha.year) + str (fecha.month) + str (fecha.day)
    hit = cache.get(key)
    if (hit == None):
        data = News.objects.all().order_by('-numero_accessos')[:10]
        sedata = serializers.serialize('json',data)
        cache.set(key,sedata,60*60*24)
        return sedata
    else:
        d = json.loads(hit)
        return d
