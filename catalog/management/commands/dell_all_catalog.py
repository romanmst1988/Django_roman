from django.core.management.base import BaseCommand
from catalog.models import Catalog

class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Catalog.objects.all().delete()
        # Group.objects.all().delete()