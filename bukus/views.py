from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Buku
from django.views.generic.base import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from .forms import BukuForm

def home(request):
    buku = Buku.objects.all()
    return render(request, 'home.html', {'buku':buku})

def index(request):
    buku = Buku.objects.all()
    return render(request, 'index.html', {'buku':buku})

def insert(request):
    if request.method=='POST':
        form = BukuForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/buku')
    else:
        form = BukuForm()
    return render(request, 'index.html', {'form': form})

def edit(request, id):  
    data = Buku.objects.get(id=id)
    return render(request, 'edit.html', {'data':data})

def update(request, id):
    buku = get_object_or_404(Buku, id=id)
    if request.method=='POST':
        form = BukuForm(request.POST or None, instance = buku) 

        if form.is_valid():
            form.save()
            return redirect('/buku')
    return render(request, 'index.html', {'form': form})

def destroy(request, id):  
    buku = Buku.objects.filter(id=id)  
    buku.delete()
    return redirect("/buku")

def TestModelListJson(BaseDatatableView):
    model = Buku