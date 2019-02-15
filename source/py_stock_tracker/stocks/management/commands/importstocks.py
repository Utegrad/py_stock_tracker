from django.core.management.base import BaseCommand, CommandError

from stocks.models import Stock


class Command(BaseCommand):
    help = 'Import stocks from csv file in import_data folder'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Expected output')
