from django import forms

class CustomerForm1(forms.Form):
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'enter the name'}))
    phone=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'enter the phone'}))
    emailid=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'enter the emailid'}))