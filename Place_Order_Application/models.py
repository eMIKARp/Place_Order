from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.

class Category(models.Model):

    DEFAULT_PK = 1

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,null=False)
    price = models.IntegerField(blank=False,null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=Category.DEFAULT_PK)

    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):

    DEFAULT_PK = 1

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    pnumber = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.pnumber+" "+self.address

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    products =  models.ManyToManyField('Product')
    status = models.BooleanField(default=False,blank=False,null=False)
    time = models.DateTimeField(blank=False, null=False,default=now)
    address=models.CharField(max_length=500,blank=False,null=False)
    pnumber = models.CharField(max_length=100, blank=False, null=False)
    user_who_placed_order = models.ForeignKey('UserProfileInfo', on_delete=models.CASCADE,default=UserProfileInfo.DEFAULT_PK)


    def __str__(self):
        return str(self.time) + " "+self.address

