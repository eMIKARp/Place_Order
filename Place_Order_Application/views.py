from django.shortcuts import render
from Place_Order_Application.forms import Create_Product_Form
from Place_Order_Application.forms import Create_Category_Form
from Place_Order_Application.forms import Create_Order_Form
from Place_Order_Application.models import Product
from Place_Order_Application.models import Category
from Place_Order_Application.models import Order


# Create your views here.

def index(request):
    context = dict()
    return render(request,'Place_Order_Application/index.html',context=context)

def place_order(request):

    form = Create_Order_Form()
    if request.method == 'POST':
        form = Create_Order_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return guest(request)
        else:
            print("Invalid form")

    context = {'form':form}
    return render(request,'Place_Order_Application/place_order.html',context=context)

def guest(request):
    context = dict()
    return render(request,'Place_Order_Application/guest.html',context=context)

def check_products(request):
    all_products = Product.objects.all()
    context = {'all_products':all_products,}
    return render(request,'Place_Order_Application/check_products.html',context=context)

def check_orders(request):

    all_orders = Order.objects.all()

    context = {'all_orders':all_orders,}
    return render(request,'Place_Order_Application/check_orders.html',context=context)

def administrator(request):
    context = dict()
    return render(request,'Place_Order_Application/administrator.html',context=context)

def add_user(request):
    context = dict()
    return render(request,'Place_Order_Application/add_user.html',context=context)

def add_product(request):
    form = Create_Product_Form()
    if request.method == "POST":
        form = Create_Product_Form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return administrator(request)
        else:
            print("Invalid form")

    context = {'form':form,}
    return render(request,'Place_Order_Application/add_product.html',context=context)

def log_in(request):
    context = dict()
    return render(request,'Place_Order_Application/log_in.html',context=context)

def check_status(request):
    context = dict()
    return render(request,'Place_Order_Application/check_status.html',context=context)


def check_categories(request):

    all_categories = Category.objects.all()

    context = {'all_categories':all_categories}
    return render(request, 'Place_Order_Application/check_categories.html', context=context)


def add_category(request):

    form = Create_Category_Form()

    if request.method == 'POST':
        form = Create_Category_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return administrator(request)
        else:
            print("Invalid form")

    context={'form':form}
    return render(request,'Place_Order_Application/add_category.html',context=context)