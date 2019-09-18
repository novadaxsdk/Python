import unittest

from novadax import RequestClient as NovaClient

ACCESS_KEY = 'your access key'
SECRET_KEY = 'your secret key'
url = "url"


class TestNovadaxApi(unittest.TestCase):
    def test_conn(self):
        client = NovaClient(ACCESS_KEY, SECRET_KEY, url)
        print(client.get_timestamp())

    def test_balance(self):
        client = NovaClient(ACCESS_KEY, SECRET_KEY, url)
        print(client.get_account_balance())

    def test_withdraw_coin(self):
        client = NovaClient(ACCESS_KEY, SECRET_KEY, url)
        print(client.withdraw_coin("USDT","1",'..'))