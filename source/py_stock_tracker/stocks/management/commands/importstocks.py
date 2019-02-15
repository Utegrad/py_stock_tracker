import re
from os import listdir, path

from django.core.management.base import BaseCommand, CommandError

from stocks.models import Stock
from stocks.constants import _DEFAULT_IMPORT_PATH


def _get_csv_files(import_path):
    all_files = [f for f in listdir(import_path) if path.isfile(path.join(import_path, f))]
    valid_extension = ['csv', 'txt', ]
    data_files = [f for f in all_files if any(f.endswith(ext) for ext in valid_extension)]
    return data_files

class Command(BaseCommand):
    help = 'Import stocks from csv file(s) in import_data folder'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='*', type=str)

    def handle(self, *args, **options):
        if len(options['path']) > 0:
            for p in options['path']:
                files = _get_csv_files(p)
        else:
            files = _get_csv_files(_DEFAULT_IMPORT_PATH)
            for f in files:
                self.stdout.write(f)


