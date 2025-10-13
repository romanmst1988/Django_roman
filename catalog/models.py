from django.db import models

class Catalog(models.Model):
    FIRST_YEAR = 'Первичная недвижимость'
    SECOND_YEAR = 'Новостройки'
    THIRD_YEAR = 'Дома со сроком эксплуатации до X лет'
    FOURTH_YEAR = 'Старый жилой фонд'

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'Первичная недвижимость'),
        (SECOND_YEAR, 'Новостройки'),
        (THIRD_YEAR, 'Дома со сроком эксплуатации до X лет'),
        (FOURTH_YEAR, 'Старый жилой фонд'),
    ]

    first_name = models.CharField(max_length=150, verbose_name='Вид недвижимости')
    last_name = models.CharField(max_length=150, verbose_name='Площадь (кв.м)', unique=True)
    year = models.CharField(
        max_length=66,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FIRST_YEAR,
        verbose_name='Состояние объекта'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'
        ordering = ['last_name']

# Поля моделей и Параметры полей
# class Group(models.Model):
#     name = models.CharField(max_length=200)
#     group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='catalogs')
#
#     def __str__(self):
#         return self.name




# class Profile(models.Model):
#     # добавьте необходимые поля
#     user_info = models.TextField(blank=True)
#
#     def __str__(self):
#         return f"Profile {self.id}"
#
#
# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Catalog(models.Model):
#         FIRST_YEAR = 'first'
#         SECOND_YEAR = 'second'
#         THIRD_YEAR = 'third'
#         FOURTH_YEAR = 'fourth'
#
#         YEAR_IN_SCHOOL_CHOICES = [
#             (FIRST_YEAR, 'Первичная недвижимость'),
#             (SECOND_YEAR, 'Новостройки'),
#             (THIRD_YEAR, 'Дома со сроком эксплуатации до X лет'),
#             (FOURTH_YEAR, 'Старый жилой фонд'),
#         ]
#
#         first_name = models.CharField(max_length=150, verbose_name='Недвижимость')
#         Last_name = models.CharField(max_length=150, verbose_name='Вид', unique=True)
#
#         age = models.IntegerField(help_text='Введите возраст постройки')
#         is_active = models.BooleanField(default=True)
#         description = models.TextField(null=True, blank=True)
#         created_at = models.DateTimeField(auto_now_add=True)
#         image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
#         group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='catalogs')
#         profile = models.OneToOneField('Profile', on_delete=models.CASCADE)
#         tags = models.ManyToManyField('Tag')
#
#         STATUS_CHOICES = [
#             ('draft', 'Draft'),
#             ('published', 'Published'),
#         ]
#         status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#
#
#         def __str__(self):
#             return f"{self.first_name} {self.Last_name}"
#
#         class Meta:
#             verbose_name = 'Каталог'
#             verbose_name_plural = 'Каталоги'
#             ordering = ['first_name']
#             db_table = 'custom_table_name'
