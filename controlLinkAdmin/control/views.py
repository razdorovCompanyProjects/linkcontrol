import pprint
from django.shortcuts import render
from django.http.response import HttpResponse
from .dataFromBitrix import DataBitrix, DataMetrika

def index(request, id):
    lead = DataBitrix(id).getData()
    metrika = DataMetrika(id).getData()
    return render(request, 'control/index.html', {'lead':len(lead),'metrika':int(metrika['max'][0]),'id':id})
    # return render(request, 'control/index.html', {'id':id})

def search(request):
    return render(request, 'control/search.html')