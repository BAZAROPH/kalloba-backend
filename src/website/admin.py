from django.contrib import admin
from .models import (Profiles, Products, Categories, Requests, Orders, DiscountCodes, Payments, Messages, Permission,
                     Stores, SubCategories)


# Register your models here.
@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'contact',
        'birth_date',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    # readonly_fields = ('daddress_descriptioneleted_at',)
    empty_display = 'Vide'


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = (
        'name',
        'slug',
        'price',
        'stock',
        'image_one',
        'image_two',
        'image_three',
        'image_four',
        'seller',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'sender',
        'recipient',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'seller',
        'client',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(DiscountCodes)
class DiscountCodesAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'min_purchase',
        'max_purchase',
        'deadline',
        'unit',
        'seller',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        'reference',
        'motif',
        'payer',
        'beneficiary',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'recipient',
        'content',
        'created_at',
        'updated_at',
        'deleted_at',
    )
    empty_display = 'Vide'


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'content_type',
        'codename',
    )
    empty_display = 'Vide'


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'status',
        'manager_contact',
        'other_contact',
        'address',
        'seller',
        'created_at',
        'updated_at',
        'deleted_at',
    )