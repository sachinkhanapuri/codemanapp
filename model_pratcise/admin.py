from django.contrib import admin
from model_pratcise.models import Customer,Order
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class Customer_Admin(ModelAdmin):
    list_display=['name','phone','emailid','date_created']
    search_fields=['name']
    list_filter=['date_created']

class Order_Admin(ModelAdmin):
    list_display=['customer','status','order_name']
    search_fields=['status']
    list_filter=['date_created']

admin.site.register(Customer,Customer_Admin)
admin.site.register(Order,Order_Admin)




