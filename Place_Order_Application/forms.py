from django import forms

from Place_Order_Application.models import Category
from Place_Order_Application.models import Product
from Place_Order_Application.models import User
from Place_Order_Application.models import Order


class Register_User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'


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
