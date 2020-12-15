from novadax.kernel import BaseHTTPClient


class RequestClient:
    def __init__(self, access_key=None, secret_key=None, endpoint='https://api.novadax.com'):
        self._client = BaseHTTPClient(endpoint, access_key, secret_key)

    def get_timestamp(self):
        return self._client.get('/v1/common/timestamp')

    def get_symbol(self, symbol):
        return self._client.get('/v1/common/symbol', {
            'symbol': symbol
        })

    def list_symbols(self):
        return self._client.get('/v1/common/symbols')

    def list_tickers(self):
        return self._client.get('/v1/market/tickers')

    def get_ticker(self, symbol):
        return self._client.get('/v1/market/ticker', {
            'symbol': symbol
        })

    def get_depth(self, symbol, limit=100):
        return self._client.get('/v1/market/depth', {
            'symbol': symbol,
            'limit': limit
        })

    def list_trades(self, symbol, limit=100):
        return self._client.get('/v1/market/trades', {
            'symbol': symbol,
            'limit': limit
        })

    def get_kline(self, symbol, unit, from_score, to_score):
        return self._client.get('/v1/market/kline/history', {
            'symbol': symbol,
            'unit': unit,
            'from': from_score,
            'to': to_score
        })

    def get_order(self, _id):
        return self._client.get_with_auth('/v1/orders/get', {
            'id': _id
        })

    def list_orders(self, symbol, status=None,
                    from_id=None, to_id=None,
                    from_timestamp=None, to_timestamp=None,
                    account_id=None, limit=100):
        return self._client.get_with_auth('/v1/orders/list', {
            'accountId': account_id,
            'symbol': symbol,
            'status': status,
            'fromId': from_id,
            'toId': to_id,
            'fromTimestamp': from_timestamp,
            'toTimestamp': to_timestamp,
            'limit': limit
        })

    def create_order(self, symbol, _type, side, price=None, amount=None, value=None, account_id=None):
        return self._client.post_with_auth('/v1/orders/create', {}, {
            'accountId': account_id,
            'symbol': symbol,
            'type': _type,
            'side': side,
            'price': price,
            'amount': amount,
            'value': value
        })

    def cancle_order(self, _id):
        return self._client.post_with_auth('/v1/orders/cancel', {}, {
            'id': _id
        })

    def list_order_fills(self, order_id=None, symbol=None,
                         from_id=None, to_id=None,
                         from_timestamp=None, to_timestamp=None,
                         account_id=None, limit=100):
        return self._client.get_with_auth('/v1/orders/fills', {
            'accountId': account_id,
            'orderId': order_id,
            'symbol': symbol,
            'fromId': from_id,
            'toId': to_id,
            'fromTimestamp': from_timestamp,
            'toTimestamp': to_timestamp,
            'limit': limit
        })

    def get_account_balance(self):
        return self._client.get_with_auth('/v1/account/getBalance')

    def get_account_balance_current(self):
        return self._client.get_with_auth('/v1/account/getBalance/current')

    def withdraw_coin(self, code, amount, toAddr, tag=None):
        return self._client.post_with_auth('/v1/account/withdraw/coin', {}, {
            'amount': amount,
            'code': code,
            'wallet': toAddr,
            'tag': tag
        })

    def subs(self):
        return self._client.get_with_auth('/v1/account/subs')

    def subs_balance(self, sub_id):
        return self._client.get_with_auth('/v1/account/subs/balance', {
            "subId": sub_id
        })

    def subs_transfer(self, sub_id, currency, transfer_amount, transfer_type):
        return self._client.post_with_auth('/v1/account/subs/transfer', {}, {
            'subId': sub_id,
            'currency': currency,
            'transferAmount': transfer_amount,
            'transferType': transfer_type
        })

    def subs_transfer_record(self, sub_id):
        return self._client.get_with_auth('/v1/account/subs/transfer/record', {
            'subId': sub_id
        })
