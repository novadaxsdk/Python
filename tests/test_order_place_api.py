import time
import math
import random
import unittest

from novadax import RequestClient as NovaClient
from tests.test_config import API_URL, ACCESS_KEY, SECRET_KEY

class TestOrderAPI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = NovaClient(ACCESS_KEY, SECRET_KEY, url=API_URL)
        self.symbols_config = {}
        for symbol_config in self.api.list_symbols()['data']:
            self.symbols_config[symbol_config['symbol']] = symbol_config

    def test_place_limit_order(self):
        try:
            print(self.api.create_order('', 'LIMIT', 'BUY', '90000', '0.001'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'LIMIT', 'BUY', '', '0.001'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'LIMIT', 'BUY', '12.121212', '0.001'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'LIMIT', 'BUY', '90000', '0.001'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'LIMIT', 'SELL', '10000', '0.001'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'LIMIT', 'SELL', '30000', ''))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'LIMIT', 'SELL', '30000', '12.12121999999'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'LIMIT', 'SELL', '30000', '0.000001'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'MARKET', 'SELL', '30000', ''))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'MARKET', 'SELL', '30000', '12121.12121211212121'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'MARKET', 'SELL', '30000', '0'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'MARKET', 'BUY', '30000', '0'))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'MARKET', 'BUY', '30000', '0', "0000.00000000001"))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'MARKET', 'BUY', '30000', '0', "1"))
        except Exception as e:
            print(str(e))
        try:
            print(self.api.create_order('BTC_BRL', 'MARKET', 'BUY', '30000', '0', "121211111121212.12"))
        except Exception as e:
            print(str(e))

