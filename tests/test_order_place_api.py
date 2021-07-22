import unittest

from novadax import RequestClient as NovaClient
from tests.test_config import REST_ENDPOINT, ACCESS_KEY, SECRET_KEY


class TestOrderAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = NovaClient(ACCESS_KEY, SECRET_KEY, endpoint=REST_ENDPOINT)
        cls.symbols_config = {}
        for symbol_config in cls.api.list_symbols()['data']:
            cls.symbols_config[symbol_config['symbol']] = symbol_config

    def test_place_limit_order(self):
        self._create_order('DAI_USD', 'LIMIT', 'BUY', price='1', amount='10')
        self._create_order('DAI_USDT', 'LIMIT', 'BUY', price='', amount='10')
        self._create_order('DAI_USDT', 'LIMIT', 'BUY', price='999999999', amount='10')
        self._create_order('DAI_USDT', 'LIMIT', 'BUY', price='1.11111', amount='10')
        self._create_order('DAI_USDT', 'LIMIT', 'BUY', price='2', amount='10')

        self._create_order('DAI_USDT', 'LIMIT', 'SELL', price='0.5', amount='10')
        self._create_order('DAI_USDT', 'LIMIT', 'SELL', price='1', amount='')
        self._create_order('DAI_USDT', 'LIMIT', 'SELL', price='1', amount='10.1111111111')
        self._create_order('DAI_USDT', 'LIMIT', 'SELL', price='1', amount='4.5')

    def test_place_market_order(self):
        self._create_order('DAI_USD', 'MARKET', 'BUY', value='10')
        self._create_order('DAI_USDT', 'MARKET', 'BUY', value='')
        self._create_order('DAI_USDT', 'MARKET', 'BUY', value='10.1111111111')
        self._create_order('DAI_USDT', 'MARKET', 'BUY', value='4.5')

        self._create_order('DAI_USD', 'MARKET', 'SELL', amount='10')
        self._create_order('DAI_USDT', 'MARKET', 'SELL', amount='')
        self._create_order('DAI_USDT', 'MARKET', 'SELL', amount='10.1111111111')
        self._create_order('DAI_USDT', 'MARKET', 'SELL', amount='1')

    def test_place_stop_limit_order(self):
        self._create_order('DAI_USD', 'STOP_LIMIT', 'BUY', price='1', amount='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='', amount='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='999999999', amount='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='1.11111', amount='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='2', amount='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='1', amount='10', operator=None, stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='1', amount='10', operator='GTE', stop_price="")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='1', amount='10', operator='GTE', stop_price="-1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='1', amount='10', operator='GTE', stop_price="999999999")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'BUY', price='1', amount='10', operator='GTE', stop_price="1.11111")

        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='0.5', amount='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='10.111111111', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='4.5', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='10', operator=None, stop_price="1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='10', operator='GTE', stop_price="")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='10', operator='GTE', stop_price="-1")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='10', operator='GTE', stop_price="999999999")
        self._create_order('DAI_USDT', 'STOP_LIMIT', 'SELL', price='1', amount='10', operator='GTE', stop_price="1.11111")

    def test_place_stop_market_order(self):
        self._create_order('DAI_USD', 'STOP_MARKET', 'BUY', value='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='10.1111111111', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='4.5', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='10', operator=None, stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='10', operator='GTE', stop_price="")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='10', operator='GTE', stop_price="-1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='10', operator='GTE', stop_price="999999999")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'BUY', value='10', operator='GTE', stop_price="1.11111")

        self._create_order('DAI_USD', 'STOP_MARKET', 'SELL', amount='10', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='10.1111111111', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='4.5', operator='GTE', stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='10', operator=None, stop_price="1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='10', operator='GTE', stop_price="")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='10', operator='GTE', stop_price="-1")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='10', operator='GTE', stop_price="999999999")
        self._create_order('DAI_USDT', 'STOP_MARKET', 'SELL', amount='10', operator='GTE', stop_price="1.11111")

    def _create_order(self, symbol, _type, side, price=None, amount=None, value=None, operator=None, stop_price=None):
        try:
            print(self.api.create_order(symbol, _type, side, price, amount, value, None, operator, stop_price))
        except Exception as e:
            print(str(e))
