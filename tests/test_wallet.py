import json
import unittest

from novadax import RequestClient as NovaClient
from tests.test_config import REST_ENDPOINT, ACCESS_KEY, SECRET_KEY


class TestWallet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = NovaClient(ACCESS_KEY, SECRET_KEY, endpoint=REST_ENDPOINT)

    def test_crypto_chain(self):
        res = self.api.crypto_chain('LINK')
        print(json.dumps(res, indent=4))

    def test_withdraw_coin(self):
        res = self.api.withdraw_coin('LINK', '2', '0x0cdc3e160ed5280937a806e0bd9f10dfcad90360', None);
        print(res)
