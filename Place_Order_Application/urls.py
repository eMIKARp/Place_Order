from django.urls import path,re_path,include
from Place_Order_Application import views

app_name='Place_Order_Application'

urlpatterns = [
    re_path(r'^index',views.index,name="index"),
    re_path(r'^place_order',views.place_order,name="place_order"),
    re_path(r'^guest',views.guest,name="guest"),
    re_path(r'^check_products',views.check_products,name="check_products"),
    re_path(r'^check_orders',views.check_orders,name="check_orders"),
    re_path(r'^administrator',views.administrator,name="administrator"),
    re_path(r'^add_user',views.add_user,name="add_user"),
    re_path(r'^add_product',views.add_product,name="add_product"),
    re_path(r'^log_in',views.log_in,name="log_in"),
    re_path(r'^log_out',views.log_out,name='log_out'),
    re_path(r'^add_category',views.add_category,name="add_category"),
    re_path(r'^check_categories',views.check_categories,name="check_categories"),

]
