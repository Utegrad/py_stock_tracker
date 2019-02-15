import os
import random
import string
import unittest
from io import StringIO

from django.core.management import call_command
from django.db import IntegrityError

from .models import Stock


def random_string(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class StockTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def test_stock_symbols_are_unique(self):
        stock_name_1 = random_string(size=24)
        stock_name_2 = random_string()
        stock_symbol = random_string(size=4)
        Stock.objects.create(name=stock_name_1, ticker=stock_symbol)
        with self.assertRaisesRegexp(IntegrityError, 'UNIQUE constraint failed'):
            Stock.objects.create(name=stock_name_2, ticker=stock_symbol)

    def test_stock_name_and_symbol_are_unique_together(self):
        stock_name1 = random_string(size=24)
        stock_ticker_1 = random_string(size=3)
        stock_ticker_2 = random_string(size=4)
        # 2 Stocks, same name, different symbol
        Stock.objects.create(name=stock_name1, ticker=stock_ticker_1)
        Stock.objects.create(name=stock_name1, ticker=stock_ticker_2)
        with self.assertRaisesRegexp(IntegrityError, 'UNIQUE constraint failed'):
            Stock.objects.create(name=stock_name1, ticker=stock_ticker_2)

    def test_command_import_stocks_no_args(self):
        try:
            call_command('importstocks', )
        except Exception:
            self.fail("importstocks with no argument raised an exception")
