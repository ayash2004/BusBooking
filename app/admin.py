from django.contrib import admin
from .models import Ticket, Offer,Contact,Food, Profile, Register_table, Cart

# Register your models here.

admin.site.register(Ticket)

admin.site.register(Register_table)
# admin.site.register(Profile)
# admin.site.register(Cart)

# @admin.register(Offer)
# class OfferModelAdmin(admin.ModelAdmin):
#     list_display = ['id','title','discount_price','actual_price','offer_image']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','message','date']

# @admin.register(Food)
# class FoodModelAdmin(admin.ModelAdmin):
#     list_display = ['id','title','actual_price','quantity','food_image']
