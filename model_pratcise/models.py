from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=30,null=True,blank=False)
    phone=models.CharField(max_length=10,null=True,blank=False)
    emailid=models.CharField(max_length=30,null=True,blank=False)
    date_created=models.DateTimeField(auto_now=True)
   



class Order(models.Model):
    choices1=(
        ('pending','pending'),
        ('out of delivery','out of delivery'),
        ('Delivered','Delivered'),
    )
    choices2=(
        ('BBQ chicken','BBQ  chicken'),
        ('Chicken chily','Chicken chilly'),
        ('butter chicken','butter chicken'),
        ('chicken loppy','chicken loppy'),
        ('chicken masala','chicken masala'),
    )

    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_name=models.CharField(max_length=30,choices=choices2)
    address=models.TextField(null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=choices1)




