from novadax.impl import HTTPClient

class RequestClient(object):
    def __init__(self, access_key = None, secret_key = None, url = 'https://api.novadax.com'):
        self._http = HTTPClient(url, access_key, secret_key)


    def get_timestamp(self):
        return self._http.get('/v1/common/timestamp')

    def list_symbols(self):
        return self._http.get('/v1/common/symbols')


    def list_tickers(self):
        return self._http.get('/v1/market/tickers')

    def get_ticker(self, symbol):
        return self._http.get('/v1/market/ticker', {
            'symbol': symbol
        })

    def get_depth(self, symbol, limit = 100):
        return self._http.get('/v1/market/depth', {
            'symbol': symbol,
            'limit': limit
        })

    def list_trades(self, symbol, limit = 100):
        return self._http.get('/v1/market/trades', {
            'symbol': symbol,
            'limit': limit
        })


    def get_order(self, _id):
        return self._http.get_with_auth('/v1/orders/get', {
            'id': _id
        })

    def list_orders(self, symbol, status = None, from_id = None, to_id = None, from_timestamp = None, to_timestamp = None, limit = 100):
        return self._http.get_with_auth('/v1/orders/list', {
            'symbol': symbol,
            'status': status,
            'fromId': from_id,
            'toId': to_id,
            'fromTimestamp': from_timestamp,
            'toTimestamp': to_timestamp,
            'limit': limit
        })

    def create_order(self, symbol, _type, side, price = None, amount = None, value = None):
        return self._http.post_with_auth('/v1/orders/create', {}, {
            'symbol': symbol,
            'type': _type,
            'side': side,
            'price': price,
            'amount': amount,
            'value': value
        })

    def cancle_order(self, _id):
        return self._http.post_with_auth('/v1/orders/cancel', {}, {
            'id': _id
        })

    def list_order_fills(self, _id):
        return self._http.get_with_auth('/v1/orders/fill', {
            'id': _id
        })


    def get_account_balance(self):
        return self._http.get_with_auth('/v1/account/getBalance')
