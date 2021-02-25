from django.shortcuts import render
from django.http import HttpResponse
from .models import Buku
from django.views.generic.base import TemplateView

def home(request):
    return HttpResponse('Hello, World!')

def index(request):
    bukus = Buku.objects.all()
    return render(request, 'index.html', {'bukus':bukus})