from django.db import models

class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование объекта недвижимости",
        help_text="Введите наименование объекта недвижимости",
    )  # Поле для названия
    description = models.TextField(
        max_length=300,
        verbose_name="Описание объекта недвижимости",
        help_text="Введите описание объекта недвижимости",
        null=True,
        blank=True,
    )  # Поле для описания
    image = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
        verbose_name="Фото объекта недвижимости",
        help_text="Загрузите фото объекта недвижимости",
    )  # Поле для загрузки изображения
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )  # Связь с моделью Category
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена объекта недвижимости",
        help_text="Введите цену объекта недвижимости",
    )  # Поле для цены
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания объекта недвижимости",
        help_text="Введите дату создания объекта недвижимости",
        blank=True,
        null=True,
    )  # Дата создания
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения объекта недвижимости",
        help_text="Введите дату последнего изменения объекта недвижимости",
        blank=True,
        null=True,
    )  # Дата последнего изменения

    def __str__(self):
        return f"Продукт - {self.name}, Категория продукта - {self.category}"

    class Meta:
        verbose_name = "Объект Недвижимости"
        verbose_name_plural = "Объекты Недвижимости"
        ordering = ["name", "category"]


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Категория Недвижимости",
        help_text="Введите категорию",
    )  # Поле для названия
    description = models.TextField(
        max_length=200,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        null=True,
        blank=True,
    )  # Поле для описания

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория Недвижимости"
        verbose_name_plural = "Категории Недвижимости"
        ordering = ["name"]


# Создаем модель контактных данных
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название организации")
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    working_hours = models.CharField(max_length=100, verbose_name="Режим работы")
    map_code = models.TextField(
        blank=True, null=True, verbose_name="Код карты (iframe)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
