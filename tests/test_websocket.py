import unittest

from novadax import WebSocketClient
from tests.test_config import *


def message_handler(msg):
    print('Received message: ', type(msg), msg)


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.api = WebSocketClient(ACCESS_KEY, SECRET_KEY, endpoint=WEB_SOCKET_ENDPOINT)

    def test_sub_market_tickers(self):
        self.api.sub_market_tickers(message_handler)

    def test_sub_market_ticker(self):
        self.api.sub_market_ticker("BTC_BRL", message_handler)

    def test_sub_market_depth(self):
        self.api.sub_market_depth("BTC_BRL", message_handler)

    def test_sub_market_trade(self):
        self.api.sub_market_trade("BTC_BRL", message_handler)

    def test_sub_market_kline(self):
        self.api.sub_market_kline("BTC_BRL", "1M", message_handler)
