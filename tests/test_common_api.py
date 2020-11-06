import time
import unittest

from novadax import RequestClient as NovaClient
from tests.test_config import REST_ENDPOINT, ACCESS_KEY, SECRET_KEY


class TestCommonAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = NovaClient(ACCESS_KEY, SECRET_KEY, endpoint=REST_ENDPOINT)

    def are_dict_type_equal(self, first_dict, second_dict):
        self.assertCountEqual(first_dict.keys(), second_dict.keys())
        for item_key in first_dict.keys():
            if first_dict[item_key] is not None and second_dict[item_key] is not None:
                self.assertIsInstance(first_dict[item_key], second_dict[item_key].__class__)

    def test_get_symbol(self):
        response = self.api.get_symbol('BTC_BRL')
        self.are_dict_type_equal(response['data'], {
            "symbol": "BTC_BRL",
            "status": "ONLINE",
            "baseCurrency": "BTC",
            "quoteCurrency": "BRL",
            "amountPrecision": 4,
            "pricePrecision": 2,
            "valuePrecision": 4,
            "minOrderAmount": "0.001",
            "minOrderValue": "5",
        })

    def test_list_symbols(self):
        response = self.api.list_symbols()
        self.assertLessEqual(0, len(response['data']))

        for symbol in response['data']:
            self.are_dict_type_equal(symbol, {
                "symbol": "BTC_BRL",
                "status": "ONLINE",
                "baseCurrency": "BTC",
                "quoteCurrency": "BRL",
                "amountPrecision": 4,
                "pricePrecision": 2,
                "valuePrecision": 4,
                "minOrderAmount": "0.001",
                "minOrderValue": "5",
            })

    def test_get_timestamp(self):
        response = self.api.get_timestamp()
        self.assertTrue(abs(response['data'] / 1000 - time.time()) < 60)
