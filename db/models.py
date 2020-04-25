from django.db import models

# Create your models here.
buylist=[
    ("JILA","JILA MD UNION TEST ADDREESS \n GST NO : !12343557 \n TESTING"),
]
selllist=[
    ("PARESH","PARESHTRADERS SELLER SELECTED \n BHOPAL \n \n (*@^)%!#@@ ")
]
stat= [
    (1,"PAID"),
    (0,"UNPAID")
]

class Billing(models.Model):
    invoice=models.IntegerField(primary_key=True)
    buyer=models.CharField(max_length=300,choices=buylist)
    seller=models.CharField(max_length=300,choices=selllist)
    challan_no=models.IntegerField()
    buyer_order_no=models.IntegerField()
    invoice_date=models.DateField()
    delivery_date=models.DateField()
    order_date=models.DateField()
    notes=models.TextField()
    status=models.BooleanField(default=0,choices=stat)

    def __str__(self):
        return str(self.invoice)

class Products(models.Model):
    invoice=models.ForeignKey(Billing,on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    quantity=models.FloatField()
    rate=models.FloatField()
    unit=models.CharField(max_length=50)
    gst=models.FloatField()
    discount=models.FloatField()
    sub_total=models.FloatField()
    total=models.FloatField()
    words=models.CharField(max_length=100)

    def __str__(self):
        return str(self.total)

    
    




    




