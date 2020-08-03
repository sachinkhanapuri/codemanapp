from django.shortcuts import render,redirect
from model_pratcise.models import Customer,Order
from model_pratcise.forms import CustomerForm,OrderForm,SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
 


# Create your views here.
def homepage(request):
    return render(request,'model_pratcise/home.html')

def register(request): 
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password1=request.POST['password1']
            password2=request.POST['password2']
            emailid=request.POST['emailid']
            user=User.objects.create_user(username=username,password=password1,email=emailid)
            user.save()
            messages.success(request,"successfully create registeration")
            return redirect('login')
    else:
        form=SignupForm()
    return render(request,'model_pratcise/register.html',{'form':form})

def login(request):
 
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request,'invalid username and password')
                return redirect('login')
    else:
        form=LoginForm()
    return render(request,'model_pratcise/login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('homepage')

def index(request):

    customer=Customer.objects.all()
    customer_count=customer.count()
   
    order=Order.objects.all()
    order_count=order.count()

    pending_status=Order.objects.filter(status="pending")
    pending_status_count=pending_status.count()

    Delivered_status=Order.objects.filter(status="Delivered")
    Delivered_status_count=Delivered_status.count()

    Out_of_Delivered_status=Order.objects.filter(status="out of delivery")
    Out_of_Delivered_status_count=Out_of_Delivered_status.count()

    return render (request,'model_pratcise/index.html',{'customer':customer,'customer_count':customer_count, 'order':order,'order_count':order_count ,'pending_status_count':pending_status_count,'Delivered_status_count':  Delivered_status_count,'Out_of_Delivered_status_count': Out_of_Delivered_status_count})


@login_required
def customer_list(request):
    form=CustomerForm()
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=CustomerForm()
    return render(request,'model_pratcise/form.html',{'form':form})

@login_required
def customer_edit(request,id):
    customer=Customer.objects.get(pk=id)
    form=CustomerForm(instance=customer)
    return render(request,'model_pratcise/customer_edit.html',{'customer':customer,'form':form})


@login_required
def customer_update(request,id):
    customer=Customer.objects.get(pk=id)
    form=CustomerForm(instance=customer)
    if request.method=="POST":
        form=CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=CustomerForm()
    return render(request,'model_pratcise/customer_edit.html',{'customer':customer,'form':form})


@login_required
def customer_delete(request,id):
    customer=Customer.objects.get(pk=id)
    if request.method=='POST':
        customer.delete()
        return redirect('index')
    else:
        return render(request,'model_pratcise/customer_delete.html',{'customer':customer})


@login_required
def customer_detail(request,id):
    customer1=Customer.objects.get(pk=id) 
    customer_detail=customer1.order_set.all()
    order_count1=customer_detail.count()
    return render(request,'model_pratcise/customer_detail.html',{'customer1':customer1,'customer_detail':customer_detail,'order_count1':order_count1})

def order_detail(request):
    order=Order.objects.all()
    return render(request,'model_pratcise/order_detail.html',{'order':order})
    

def order_list(request):
    if request.method=="POST":
        form1=OrderForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('index')
    else:
        form1=OrderForm()
    return render(request,'model_pratcise/form.html',{'form1':form1})


def order_edit(request,id):
    order=Order.objects.get(pk=id)
    form1=OrderForm(instance=order)
    return render(request,'model_pratcise/order_edit.html',{'order':order,'form1':form1})


def order_update(request,id):
    if request.method=="POST":
        order=Order.objects.get(pk=id)
        form1=OrderForm(instance=order,data=request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('index')
    else:
        form1=OrderForm()
    return render(request,'model_pratcise/order_edit.html',{'order':order,'form1':form1})


def order_delete(request,id):
    order=Order.objects.get(pk=id)
    if request.method=="POST":
        order.delete()
        return redirect('index')

    return render(request,'model_pratcise/order_delete.html',{'order':order})


