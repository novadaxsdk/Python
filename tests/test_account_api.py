import unittest

from novadax import RequestClient as NovaClient
from tests.test_config import API_URL, ACCESS_KEY, SECRET_KEY

class TestAccountAPI(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.api = NovaClient(ACCESS_KEY, SECRET_KEY, url=API_URL)

    def test_balance(self):
        print(self.api.get_account_balance())

    def test_withdraw_coin(self):
        print(self.api.withdraw_coin("USDT","1",'..'))
