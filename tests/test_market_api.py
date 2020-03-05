import unittest

from novadax import RequestClient as NovaClient
from tests.test_config import API_URL, ACCESS_KEY, SECRET_KEY

class TestMarketAPI(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.api = NovaClient(ACCESS_KEY, SECRET_KEY, url=API_URL)

    def are_dict_type_equal(self, first_dict, second_dict):
        self.assertCountEqual(first_dict.keys(), second_dict.keys())
        for item_key in first_dict.keys():
            if first_dict[item_key] is not None and second_dict[item_key] is not None:
                self.assertIsInstance(first_dict[item_key], second_dict[item_key].__class__)

    def test_list_tickers(self):
        response = self.api.list_tickers()
        self.assertLessEqual(0, len(response['data']))
        for symbol in response['data']:
            self.are_dict_type_equal(symbol, {
                "ask": "",
                "baseVolume24h": "10.9",
                "bid": "12000",
                "high24h": "16000",
                "lastPrice": "13000",
                "low24h": "12000",
                "open24h": "45699.47",
                "quoteVolume24h": "0",
                "symbol": "BTC_BRL",
                "timestamp": 1565071855378
            })
    
    def test_get_ticker(self):
        symbols = ['BTC_BRL', 'ETH_BTC', 'XLM_ETH']
        for symbol in symbols:
            response = self.api.get_ticker(symbol)
            self.are_dict_type_equal(response['data'], {
                "ask": "",
                "baseVolume24h": "10.9",
                "bid": "12000",
                "high24h": "16000",
                "lastPrice": "13000",
                "low24h": "12000",
                "open24h": "45699.47",
                "quoteVolume24h": "0",
                "symbol": "BTC_BRL",
                "timestamp": 1565071855378
            })
    
    def test_get_depth(self):
        symbols = ['BTC_BRL', 'ETH_BTC', 'XLM_ETH']
        for symbol in symbols:
            response = self.api.get_depth(symbol)
            self.are_dict_type_equal(response['data'], {
                "asks": [
                    ["43687.16", "0.5194"],
                    ["43687.2", "1.3129"]
                ],
                "bids": [
                    ["43657.57", "0.6135"],
                    ["43657.46", "0.0559"]
                ],
                "timestamp": 1565057338020
            })
            self.assertEqual(len(response['data']['asks'][0]), 2)
            self.assertEqual(len(response['data']['bids'][0]), 2)

    def test_list_trades(self):
        symbols = ['BTC_BRL', 'ETH_BTC', 'XLM_ETH']
        for symbol in symbols:
            response = self.api.list_trades(symbol)
            self.assertLessEqual(0, len(response['data']))
            
            for trade in response['data']:
                self.are_dict_type_equal(trade, {
                    "price": "43657.57",
                    "amount": "1",
                    "side": "SELL",
                    "timestamp": 1565007823401
                })
