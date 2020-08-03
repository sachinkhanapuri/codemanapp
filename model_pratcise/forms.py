from model_pratcise.models import Customer,Order
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','phone','emailid']
        widgets={
        'name':forms.TextInput(attrs={'placeholder':'enter the name'}),
        'phone':forms.TextInput(attrs={'placeholder':'enter the phone'}),
        'emailid':forms.TextInput(attrs={'placeholder':'enter the emailid'}),       
                }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['customer','order_name','status']


class SignupForm(UserCreationForm):
    emailid=forms.CharField(max_length=40)
    class Meta:
        model=User
        fields=['username','emailid','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'enter username'}))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'palceholder':'enter password'}))
