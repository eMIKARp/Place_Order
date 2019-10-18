from django.shortcuts import render
from Place_Order_Application.forms import Create_Product_Form
from Place_Order_Application.forms import Create_Category_Form
from Place_Order_Application.forms import Create_Order_Form
from Place_Order_Application.forms import Register_User_Form
from Place_Order_Application.forms import User_Profile_Info_Form
from Place_Order_Application.models import Product
from Place_Order_Application.models import Category
from Place_Order_Application.models import Order

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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

@login_required
def administrator(request):
    context = dict()
    return render(request,'Place_Order_Application/administrator.html',context=context)

def add_user(request):


    if request.method == 'POST':
        main_form = Register_User_Form(request.POST)
        additional_info_form = User_Profile_Info_Form(request.POST)

        if main_form.is_valid() and additional_info_form.is_valid():
            user = main_form.save()
            user.set_password(user.password)
            user.save()

            additional_info = additional_info_form.save(commit=False)
            additional_info.user=user

            if 'picture' in request.FILES:
                additional_info.picture = request.FILES['picture']
            additional_info.save()

            return render(request,'Place_Order_Application/guest.html')


        else:
            print("Form is invalid: ",main_form.errors,additional_info_form.errors)
    else:
        main_form = Register_User_Form()
        additional_info_form = User_Profile_Info_Form()

    context = {'main_form':main_form,'additional_info_form':additional_info_form}
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

@login_required()
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def log_in(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse(index))
            else: HttpResponse('Account Not Active')
        else:
            HttpResponse('Invalid login details supplied')
    else:
        return render(request,'Place_Order_Application/log_in.html',{})


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