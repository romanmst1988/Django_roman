from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200) # Поле для названия
    description = models.TextField(null=True, blank=True) # Поле для описания
    image = models.ImageField(upload_to='photos/', verbose_name='Фотография') # Поле для загрузки изображения
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products') # Связь с моделью Category
    price = models.DecimalField(max_digits=10, decimal_places=2) #Поле для цены
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объект Недвижимости'
        verbose_name_plural = 'Объекты Недвижимости'
        ordering = ['name']

class Category(models.Model):
    # first_name = models.CharField(max_length=150, verbose_name='Вид недвижимости')
    # last_name = models.CharField(max_length=150, verbose_name='Площадь (кв.м)', unique=True)
    name = models.CharField(max_length=150, verbose_name='Категория Недвижимости')
    description = models.TextField(null=True, blank=True) #Поле для описания

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория Недвижимости'
        verbose_name_plural = 'Категории Недвижимости'







# class Group(models.Model):
#     name = models.CharField(max_length=200)
#     group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='catalogs')
#
#     def __str__(self):
#         return self.name
