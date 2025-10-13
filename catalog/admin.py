from django.contrib import admin
from .models import Catalog

# самый простой способ
# admin.site.register(Catalog)


# второй простой способ обширный и гибкий с декоратором
@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year')
    list_filter = ('year',)
    search_fields = ('first_name', 'last_name',)
