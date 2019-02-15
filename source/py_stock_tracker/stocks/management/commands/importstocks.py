import csv

from os import listdir, path
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from stocks.constants import _DEFAULT_IMPORT_PATH
from stocks.models import Stock


def _get_csv_files(import_path):
    all_files = [f for f in listdir(import_path) if path.isfile(path.join(import_path, f))]
    valid_extension = ['csv', 'txt', ]
    data_files = [f for f in all_files if any(f.endswith(ext) for ext in valid_extension)]
    data_file_paths = []
    for f in data_files:
        p = path.join(_DEFAULT_IMPORT_PATH, f)
        data_file_paths.append(p)
    return data_file_paths


class Command(BaseCommand):
    help = 'Import stocks from csv file(s) in import_data folder'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str, default=_DEFAULT_IMPORT_PATH)

    def handle(self, *args, **options):
        files = _get_csv_files(options['path'])
        failed_adds = []
        successful_adds = 0
        for f in files:
            self.stdout.write(f)
            with open(f, newline='' ) as csv_file:
                dialect = csv.Sniffer().sniff(csv_file.read(1024))
                csv_file.seek(0)
                reader = iter(csv.reader(csv_file, dialect))
                next(reader)
                for row in reader:
                    msg = "Adding {} : {} to database".format(row[0], row[1])
                    # self.stdout.write(msg)
                    try:
                        Stock.objects.update_or_create(symbol=row[0], name=row[1], )
                        successful_adds += 1
                    except IntegrityError as E:
                        msg = "Failed to add {} : {} to database".format(row[0], row[1])
                        self.stderr.write(msg)
                        self.stderr.write(str(E))
                        failed_adds.append(row[1])
        self.stdout.write("Successfully added {} records".format(str(successful_adds)))
        msg = "Failed to add {} records".format(len(failed_adds))
        self.stdout.write(msg)
        for fail in failed_adds:
            self.stdout.write(fail)
