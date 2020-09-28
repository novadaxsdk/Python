import unittest

from novadax import RequestClient as NovaClient
from tests.test_config import API_URL, ACCESS_KEY, SECRET_KEY


class TestAccountAPI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = NovaClient(ACCESS_KEY, SECRET_KEY, url=API_URL)

    def are_dict_type_equal(self, first_dict, second_dict):
        self.assertCountEqual(first_dict.keys(), second_dict.keys())
        for item_key in first_dict.keys():
            if first_dict[item_key] is not None and second_dict[item_key] is not None:
                self.assertIsInstance(first_dict[item_key], second_dict[item_key].__class__)

    def test_get_account_balance(self):
        get_account_balance_response = self.api.get_account_balance()
        print(get_account_balance_response)

        '''
        for account in get_account_balance_response['data']:
            self.are_dict_type_equal(account, {
                "currency": "BTC",
                "balance": "2",
                "hold": "1",
                "available": "1",
                "accountId": "DA001"
            })
        '''

    def test_withdraw_coin(self):
        print(self.api.withdraw_coin("ETC", "0.5",
                                     '0x4d41b6faa5719b104d326fe5be9661b1314e2206'))

    def test_get_account_balance_current(self):
        balanceWithTimestamp = self.api.get_account_balance_current()
        print(balanceWithTimestamp)
