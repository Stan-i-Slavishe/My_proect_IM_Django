from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', "created", "updated", 'discount', 'on_sale']
    list_filter = ['available', 'created', 'updated', 'on_sale']
    list_editable = ['price', 'discount', 'available', 'on_sale']
    prepopulated_fields = {'slug': ('name',)}
