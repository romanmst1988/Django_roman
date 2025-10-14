from django.contrib import admin
from .models import Category, Product, Contact


@admin.register(Product)  # декоратор для регистрации модели
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")  # поля для отображения в админке
    search_fields = ("name", "description")  # поиск по имени и писанию
    list_filter = ("category",)


@admin.register(Category)  # декоратор для регистрации модели
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # поля для отображения в админке
    search_fields = ("name", "description")  # поиск по имени и описанию


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'phone', 'email')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'is_active')
        }),
        ('Контактные данные', {
            'fields': ('address', 'phone', 'email', 'working_hours')
        }),
        ('Карта', {
            'fields': ('map_code',),
            'classes': ('collapse',)
        }),
    )
