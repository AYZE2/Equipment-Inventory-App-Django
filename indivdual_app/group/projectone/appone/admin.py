from django.contrib import admin
from .models import Item , Reservation , Profile,Product
# Register your models here.

admin.site.site_header = "Inventory Admin Mangment"

admin.site.register(Item)
admin.site.register(Reservation)
admin.site.register(Profile)
admin.site.register(Product)