from django.db import models
from enum import Enum

class buyerlist(Enum):
    JILA = "JILA MD UNION TEST ADDREESS \n GST NO : !12343557 \n TESTING"
    MD = "MD \n TESTING \n GST : 1234568"
    @classmethod
    def choices(cls):
        return tuple((i.name,i.value) for i in cls)

class sellerlist(Enum):
    PARESH = "PARESHTRADERS SELLER SELECTED \n BHOPAL \n \n (*@^)%!#@@ "
    @classmethod
    def choices(cls):
        return tuple((i.name,i.value) for i in cls)

class stat(Enum):
    U="UNPAID"
    P="PAID"
    @classmethod
    def choices(cls):
        return tuple((i.name,i.value) for i in cls)

class Billing(models.Model):
    
    buyer=models.TextField(choices=buyerlist.choices())
    seller=models.TextField(choices=sellerlist.choices())
    invoice=models.IntegerField(primary_key=True)
    challan_no=models.IntegerField()
    buyer_order_no=models.IntegerField()
    invoice_date=models.DateField()
    delivery_date=models.DateField()
    order_date=models.DateField()
    notes=models.TextField()
    gst=models.FloatField()
    gstamt=models.FloatField()
    discount=models.FloatField(default=0.0)
    sub_total=models.FloatField()
    total=models.FloatField()
    words=models.CharField(max_length=100,blank=True, null=True)
    status=models.CharField(max_length=6,choices=stat.choices())


class Products(models.Model):

    invoice=models.ForeignKey(Billing,on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    quantity=models.FloatField()
    rate=models.FloatField()
    unit=models.CharField(max_length=50)
    


    
    




    




