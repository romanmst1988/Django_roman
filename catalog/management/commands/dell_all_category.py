from django.core.management.base import BaseCommand
from catalog.models import Category

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        # Group.objects.all().delete()