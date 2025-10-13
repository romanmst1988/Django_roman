from django.contrib import admin
from .models import Product, Category

# самый простой способ
# admin.site.register(Product, Category) # регистрируем модель в админке

# второй простой способ обширный и гибкий с декоратором
@admin.register(Product) # декоратор для регистрации модели
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at') # поля для отображения в админке
    list_display_links = ('name', 'description') # ссылки на редактирование
    list_editable = ('price',) # поля для редактирования
    list_per_page = 10 # количество записей на странице
    search_fields = ('name', 'description', 'category__name') # поиск по имени, описанию и категории
    list_filter = ('category', 'created_at', 'updated_at') # фильтр по категории, дате создания и изменения

@admin.register(Category) # декоратор для регистрации модели
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') # поля для отображения в админке
    search_fields = ('name', 'description') # поиск по имени и описанию