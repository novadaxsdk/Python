from novadax.kernel.websocket import BaseWebSocketClient


class WebSocketClient:
    def __init__(self, access_key=None, secret_key=None, endpoint='wss://api.novadax.com'):
        self._client = BaseWebSocketClient(endpoint)

    def sub_market_tickers(self, callback):
        self._client.subscribe("MARKET.TICKERS", callback)

    def sub_market_ticker(self, symbol, callback):
        self._client.subscribe(f"MARKET.{symbol}.TICKER", callback)

    def sub_market_depth(self, symbol, callback):
        self._client.subscribe(f"MARKET.{symbol}.DEPTH.LEVEL0", callback)

    def sub_market_trade(self, symbol, callback):
        self._client.subscribe(f"MARKET.{symbol}.TRADE", callback)
