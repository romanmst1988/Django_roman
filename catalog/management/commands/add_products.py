from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Полностью очищает базу данных и добавляет новые продукты из фикс туры"

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "catalog_fixture.json")

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены из файла"))