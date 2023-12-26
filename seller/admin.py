from django.contrib import admin
from .models import Product, Seller, Condition, ProductImage, Category, Offer, Order, Transaction, Rating, Message, Price, Amount, Order_date, Order_status, Status, Payment_method, Quantity, Payment, Buyer, Transaction_status


class SellerAdmin(admin.ModelAdmin):
    list_display = (
       'name',
        'bio',
        'email',
        'phone',
        'image_url',
        'address',
        'website'
    )



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'condition',
        'category'
    )

class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'discount',
        'description'
    )

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'amount',
        'payment_method'
    )

class QuantityAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity'
    )


class Order_dateAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'datetime'
    )

class Order_statusAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'status'
    )


class BuyerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'payment_method',
        'phone',
        'email'
    )

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'buyer',
        'product',
        'price',
        'quantity',
        'payment_method',
        'amount',
        'order_date',
        'order_status'
    )


class Transaction_statusAdmin(admin.ModelAdmin):
    list_display = (
        'payment_method',
        'status'
    )


admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Condition)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction)
admin.site.register(Rating)
admin.site.register(Message)
admin.site.register(Price)
admin.site.register(Amount)
admin.site.register(Order_date, Order_dateAdmin)
admin.site.register(Order_status, Order_statusAdmin)
admin.site.register(Status)
admin.site.register(Payment_method)
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Transaction_status, Transaction_statusAdmin)



