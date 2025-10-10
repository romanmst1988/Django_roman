from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Catalog(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='catalogs')

    def __str__(self):
        return self.name

# Поля моделей и Параметры полей

    # first_name = models.CharField(max_length=150, verbose_name='Недвижимость')
    # Last_name = models.CharField(max_length=150, verbose_name='Вид', unique=True)
    #
    # age = models.IntegerField(help_text='Введите возраст постройки')
    # is_active = models.BooleanField(default=True)
    # description = models.TextField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
    # group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='catalogs')
    # profile = models.OneToOneField('Profile', on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tag')
    #
    # STATUS_CHOICES = [
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # ]
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    #
    #
    # def __str__(self):
    #     return f"{self.first_name} {self.Last_name}"
    #
    # class Meta:
    #     verbose_name = 'Каталог'
    #     verbose_name_plural = 'Каталоги'
    #     ordering = ['first_name']
    #     db_table = 'custom_table_name'


