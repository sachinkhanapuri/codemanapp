from django.db import models

# Create your models here.
class Customer1(models.Model):
    name=models.CharField(max_length=30,null=True,blank=False)
    phone=models.CharField(max_length=10,null=True,blank=False)
    emailid=models.CharField(max_length=30,null=True,blank=False)

   
    def __str__(self):
        return self.name
