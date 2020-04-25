from django.shortcuts import render
from .models import Billing,Products,buyerlist
from django.http import HttpResponse
# Create your views here.
def show(request):
    return render(request,'billing/show.html')

def billing(request):
    d=dict()
    for i in buyerlist:
        d[i.name]=i.value
    context={
        'buyer':d,
    }
    return render(request,'billing/billing.html',context)

def convertlist(l):
    return l.split(",")


def calculation(request):
    try:
        if request.method=="GET":
            pdata=request.GET['pdata']
            bdata=request.GET['bdata']

            p=(convertlist(pdata))
            b=(convertlist(bdata))

            bill=Billing.objects.create(buyer=b[6],seller='PARESH',invoice=b[0],challan_no=b[2],buyer_order_no=b[4],invoice_date=b[1],delivery_date=b[3],order_date=b[5],notes=b[7],gst=b[9],discount=b[10],sub_total=b[8],total=b[12],status='U',gstamt=b[11])
    
            for i in range(0,len(p),5):
                Products.objects.create(invoice=bill,product=p[i],quantity=p[i+1],rate=p[i+2],unit=p[i+3])

        return HttpResponse("true")
    except ValueError as e:
        print(e)
        return HttpResponse("false")
