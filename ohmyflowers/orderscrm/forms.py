from django import forms
from .models import Company, Order, Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'position', 'company']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'rows': 8}),
            'company': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 4})
        }


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_title', 'place_title', 'address', 'payment_details']
        widgets = {
            'company_title': forms.TextInput(attrs={'class': 'form-control'}),
            'place_title': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_details': forms.TextInput(attrs={'class': 'form-control'})
        }


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['company', 'customer', 'order_list', 'order_sum', 'payment_sum', 'offer', 'payment', 'payment_done',
                  'order_completed', 'order_done', 'canceled']

        widgets = {
            'order_list': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'order_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'offer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'payment': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'payment_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'canceled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))