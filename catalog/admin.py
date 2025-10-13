from django.contrib import admin
from .models import Catalog

# самый простой способ
# admin.site.register(Catalog) # регистрируем модель в админке


# второй простой способ обширный и гибкий с декоратором
@admin.register(Catalog) # декоратор для регистрации модели
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year')
    list_filter = ('year',) # фильтр по году (добавить в строку поиска)
    search_fields = ('first_name', 'last_name',) # поиск по имени и фамилии