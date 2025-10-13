from django.core.management.base import BaseCommand
from catalog.models import Catalog

class Command(BaseCommand):
    help = 'Add test catalogs to the database'

    def handle(self, *args, **kwargs):
        catalog = Catalog.objects.create(first_name='Квартира 4-к', last_name='107,3', year=Catalog.FIRST_YEAR)

        catalog = [
            {'first_name': 'Квартира 1-к', 'last_name': '39,3', 'year': Catalog.FIRST_YEAR},
            {'first_name': 'Квартира 2-к', 'last_name': '71,2', 'year': Catalog.SECOND_YEAR},
            {'first_name': 'Квартира 3-к', 'last_name': '91,8', 'year': Catalog.THIRD_YEAR},
        ]

        for catalog_data in catalog:
            catalog, created = Catalog.objects.get_or_create(**catalog_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added catalog: {catalog.first_name} {catalog.last_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Catalog already exists: {catalog.first_name} {catalog.last_name}'))