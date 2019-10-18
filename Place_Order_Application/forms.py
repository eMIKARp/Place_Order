from django import forms

from Place_Order_Application.models import Category
from Place_Order_Application.models import Product
from Place_Order_Application.models import UserProfileInfo
from django.contrib.auth.models import User
from Place_Order_Application.models import Order


class Login_Form(forms.ModelForm):
    pass


class Register_User_Form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=('username','email','password')

class User_Profile_Info_Form(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields=('picture','pnumber','address')


class Create_Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields="__all__"


class Create_Category_Form(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"


class Create_Order_Form(forms.ModelForm):
    class Meta:
        model = Order
        exclude=('status','time','user_who_placed_order')
