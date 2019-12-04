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

    def are_dict_type_equal(self, first_dict, second_dict):
        self.assertCountEqual(first_dict.keys(), second_dict.keys())
        for item_key in first_dict.keys():
            if first_dict[item_key] is not None and second_dict[item_key] is not None:
                self.assertIsInstance(first_dict[item_key], second_dict[item_key].__class__)

    def test_place_limit_order(self):
        symbols = ['BTC_BRL']
        for symbol in symbols:
            symbol_config = self.symbols_config[symbol]
            side = random.choice(['BUY', 'SELL'])
            last_price = self.api.list_trades(symbol, 1)['data'][0]['price']
            price = math.ceil(float(last_price) * 0.91) if side == 'BUY' else math.floor(float(last_price) * 1.09)
            order_create_response = self.api.create_order(symbol, 'LIMIT', side, price = price, amount = symbol_config['minOrderAmount'])
            self.are_dict_type_equal(order_create_response['data'], {
                "id": "608695623247466496",
                "symbol": "BTC_BRL",
                "type": "MARKET",
                "side": "SELL",
                "price": "0",
                "averagePrice": "0",
                "amount": "0.123",
                "filledAmount": "0",
                "value": "0",
                "filledValue": "0",
                "filledFee": "0",
                "status": "PROCESSING",
                "timestamp": 1565165945588
            })

            time.sleep(1)

            order_cancle_response = self.api.cancle_order(order_create_response['data']['id'])
            self.assertTrue(order_cancle_response['data']['result'])

            order_get_response = self.api.get_order(order_create_response['data']['id'])
            self.are_dict_type_equal(order_get_response['data'], {
                "id": "608695623247466496",
                "symbol": "BTC_BRL",
                "type": "MARKET",
                "side": "SELL",
                "price": "0",
                "averagePrice": "0",
                "amount": "0.123",
                "filledAmount": "0",
                "value": "0",
                "filledValue": "0",
                "filledFee": "0",
                "status": "PROCESSING",
                "timestamp": 1565165945588
            })

    def test_place_market_buy_order(self):
        symbols = ['BTC_BRL']
        for symbol in symbols:
            symbol_config = self.symbols_config[symbol]
            order_create_response = self.api.create_order(symbol, 'MARKET', 'BUY', value = symbol_config['minOrderValue'])
            self.are_dict_type_equal(order_create_response['data'], {
                "id": "608695623247466496",
                "symbol": "BTC_BRL",
                "type": "MARKET",
                "side": "SELL",
                "price": "0",
                "averagePrice": "0",
                "amount": "0.123",
                "filledAmount": "0",
                "value": "0",
                "filledValue": "0",
                "filledFee": "0",
                "status": "PROCESSING",
                "timestamp": 1565165945588
            })

            time.sleep(1)

            order_fills_response = self.api.list_order_fills(order_create_response['data']['id'])
            for fill in order_fills_response['data']:
                self.are_dict_type_equal(fill, {
                    "id": "608717046691139584",
                    "orderId": "608716957545402368",
                    "symbol": "BTC_BRL",
                    "side": "BUY",
                    "amount": "0.0988",
                    "price": "45514.76",
                    "fee": "0.0000988 BTC",
                    "role": "MAKER",
                    "timestamp": 1565171053345
                })

    def test_place_market_sell_order(self):
        symbols = ['BTC_BRL']
        for symbol in symbols:
            symbol_config = self.symbols_config[symbol]
            order_create_response = self.api.create_order(symbol, 'MARKET', 'SELL', amount = symbol_config['minOrderAmount'])
            self.are_dict_type_equal(order_create_response['data'], {
                "id": "608695623247466496",
                "symbol": "BTC_BRL",
                "type": "MARKET",
                "side": "SELL",
                "price": "0",
                "averagePrice": "0",
                "amount": "0.123",
                "filledAmount": "0",
                "value": "0",
                "filledValue": "0",
                "filledFee": "0",
                "status": "PROCESSING",
                "timestamp": 1565165945588
            })

            time.sleep(1)

            order_fills_response = self.api.list_order_fills(order_create_response['data']['id'])
            for fill in order_fills_response['data']:
                self.are_dict_type_equal(fill, {
                    "id": "608717046691139584",
                    "orderId": "608716957545402368",
                    "symbol": "BTC_BRL",
                    "side": "BUY",
                    "amount": "0.0988",
                    "price": "45514.76",
                    "fee": "0.0000988 BTC",
                    "role": "MAKER",
                    "timestamp": 1565171053345
                })

    def test_list_orders(self):
        symbols = ['BTC_BRL']
        for symbol in symbols:
            list_orders_response = self.api.list_orders(symbol)
            for order in list_orders_response['data']:
                self.are_dict_type_equal(order, {
                    "id": "608695623247466496",
                    "symbol": "BTC_BRL",
                    "type": "MARKET",
                    "side": "SELL",
                    "price": "0",
                    "averagePrice": "0",
                    "amount": "0.123",
                    "filledAmount": "0",
                    "value": "0",
                    "filledValue": "0",
                    "filledFee": "0",
                    "status": "PROCESSING",
                    "timestamp": 1565165945588
                })