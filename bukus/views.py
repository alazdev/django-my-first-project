from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Buku
from django.views.generic.base import TemplateView

from .forms import BukuForm

def home(request):
    return render(request, 'home.html')

def index(request):
    bukus = Buku.objects.all()
    return render(request, 'index.html', {'bukus':bukus})

def insert(request):
    if request.method=='POST':
        form = BukuForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/buku')
    else:
        form = BukuForm()
    return render(request, 'index.html', {'form': form})