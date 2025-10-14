from django.contrib import admin

from .models import Category, Product


@admin.register(Product)  # декоратор для регистрации модели
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")  # поля для отображения в админке
    search_fields = ("name", "description")  # поиск по имени и писанию
    list_filter = ("category",)


@admin.register(Category)  # декоратор для регистрации модели
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # поля для отображения в админке
    search_fields = ("name", "description")  # поиск по имени и описанию
