from django.contrib import admin
from Place_Order_Application import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.User)
admin.site.register(models.Order)