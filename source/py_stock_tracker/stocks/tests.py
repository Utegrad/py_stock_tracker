import os
import unittest
from io import StringIO

from django.core.management import call_command
from django.db import IntegrityError

from .models import Stock


class StockTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_stock_symbols_are_unique(self):
        stock_name_1 = 'Stock 1'
        stock_name_2 = 'Stock 2'
        stock_symbol = 'blah'
        Stock.objects.create(name=stock_name_1, symbol=stock_symbol)
        with self.assertRaisesRegexp(IntegrityError, 'UNIQUE constraint failed'):
            Stock.objects.create(name=stock_name_2, symbol=stock_symbol)

    def test_stock_name_are_unique(self):
        stock_name = 'Stock'
        stock_symbol_1 = 'STK'
        stock_symbol_2 = 'STOK'
        Stock.objects.create(name=stock_name, symbol=stock_symbol_1)
        with self.assertRaisesRegexp(IntegrityError, 'UNIQUE constraint failed'):
            Stock.objects.create(name=stock_name, symbol=stock_symbol_2)

    def test_command_import_stocks_no_args(self):
        try:
            call_command('importstocks', )
        except Exception:
            self.fail("importstocks with no argument raised an exception")

    @unittest.skipUnless(os.environ['RUN_FUNCTIONAL_TESTS'] == 'True', "Not running functional tests.")
    def test_command_importstocks_opens_file(self):
        out = StringIO()
        call_command('importstocks', stdout=out, )
        self.assertIn('AMEX', out.getvalue())
