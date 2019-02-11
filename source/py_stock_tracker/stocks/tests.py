import unittest

from django.db import IntegrityError
from django.test import TestCase

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
