from django.contrib import admin
from .models import Services, Customer, Cart


@admin.register(Services)

class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','catagory', 'description','service_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city', 'state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

