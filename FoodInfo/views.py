from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def service(request):
    return render(request, 'service.html')


def search(request):
    tables = Table.objects.all()

    q = request.POST.get('q', "")

    if q:
        tables = tables.filter(name__icontains=q)
        return render(request, 'search.html', {'tables' : tables, 'q' : q})
    else:
        return render(request, 'search.html')


def addTodayFood(request):
    return None
    # foods = Food.objects.all()
    #
    # val_id = request.POST.get('val_id', "")
    #
    # if val_id:
    #     foods = foods.filter(id__icontains=val_id)
    #     return render(request, 'service.html', {'foods': foods, 'val_id': val_id})
    # else:
    #   return render(request, 'service.html')
