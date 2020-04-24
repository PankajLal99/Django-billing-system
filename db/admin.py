from django.contrib import admin
from . import models
# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    list_display=['invoice','seller','buyer']
    list_filter=['invoice_date']
    search_fields=['invoice']

    
    


admin.site.register(models.Buyer)
admin.site.register(models.Billing,BuyerAdmin)
admin.site.register(models.Products)
admin.site.register(models.Status)
admin.site.register(models.Seller)