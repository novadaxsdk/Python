import unittest

from novadax import RequestClient as NovaClient
# change
from tests.test_config import API_URL, ACCESS_KEY, SECRET_KEY


class TestAccountSubAPI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.api = NovaClient(ACCESS_KEY, SECRET_KEY, url=API_URL)

    def test_subs(self):
        subs = self.api.subs()
        print(subs)

    def test_sub_balance(self):
        subId = 'CA648855702269333504'
        ava = self.api.subs_balance(subId)
        print(ava)

    def test_sub_transfer(self):
        subId = 'CA648856083527372800'
        currency = 'BTC'
        transferAmount = '0.51'
        transferType = 'master-transfer-out'
        tid = self.api.subs_transfer(subId, currency, transferAmount, transferType);
        print(tid)

    def test_sub_transfer_record(self):
        subId = 'CA648855702269333504'
        ava = self.api.subs_transfer_record(subId)
        print(ava)
