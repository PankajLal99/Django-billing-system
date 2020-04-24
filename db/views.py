from django.shortcuts import render
from .models import Billing,Products 
from django.http import HttpResponse
# Create your views here.
def show(request):
    return render(request,'billing/show.html')

def billing(request):
    return render(request,'billing/billing.html')

def convertlist(l):
    return l.split(",")
def calculation(request):
    if request.method=="GET":
        pdata=request.GET['pdata']
        bdata=request.GET['bdata']
        tdata=request.GET['tdata']
        p=(convertlist(pdata))
        b=(convertlist(bdata))
        t=(convertlist(tdata))
        print(p,b,t)
    return HttpResponse("true")
