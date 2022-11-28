from django.contrib import admin
from .models import Item, Order, OrderPositions, Discount


class OrderPositionsInline(admin.TabularInline):
    model = OrderPositions
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'discount']
    inlines = [OrderPositionsInline]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'disc_value']
