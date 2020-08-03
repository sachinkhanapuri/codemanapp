from django.shortcuts import render,redirect
from basicform.forms import CustomerForm1
from basicform.models import Customer1
# Create your views here.

def customer_form(request):
    if request.method=="POST":
        forms=CustomerForm1(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms=CustomerForm1()
    return render(request,'basicform/form.html',{'forms':forms})

def index1(request):
    name=request.POST['name']
    phone=request.POST['phone']
    emailid=request.POST['emailid']
    content=Customer1(name=name,emailid=emailid,phone=phone)
    content.save()
    return redirect('customer_list1')

def customer_list1(request):
    customer=Customer1.objects.all()
    return render(request,'basicform/home2.html',{'customer':customer})

def customer_edit1(request,id):
    customer1=Customer1.objects.get(pk=id)
    return render(request,'basicform/customer1_edit.html',{'customer1':customer1})
   

def customer_update1(request,id):
    customer1=Customer1.objects.get(pk=id)
    customer1.name1=request.POST['name']
    customer1.phone1=request.POST['phone']
    customer1.emailid1=request.POST['emailid']
    customer1.save()
    return redirect('customer_list1')