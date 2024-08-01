from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name
    

CATEGORY = (
    ('Laptop', 'Laptop'),
    ('Mobile', 'Mobile'),
    ('StandAlone Headset', 'StandAlone Headset'),
    ('PC', 'PC'),

)
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    serial_number = models.CharField(max_length=100, null=True)
    CPU = models.CharField(max_length=100, null=True)
    GPU = models.CharField(max_length=100, null=True)
    RAM = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return f'{self.name}'


class Reservation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    staff=models.ForeignKey(User, models.CASCADE,null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item} ordered by {self.staff.username}'
    
    
class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.customer.username}-Profile'


