import unittest

from novadax import RequestClient as NovaClient
# change
from tests.test_config import REST_ENDPOINT, ACCESS_KEY, SECRET_KEY


class TestAccountSubAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = NovaClient(ACCESS_KEY, SECRET_KEY, endpoint=REST_ENDPOINT)

    def test_subs(self):
        subs = self.api.subs()
        print(subs)

    def test_sub_balance(self):
        sub_id = 'CA648855702269333504'
        ava = self.api.subs_balance(sub_id)
        print(ava)

    def test_sub_transfer(self):
        sub_id = 'CA648856083527372800'
        currency = 'BTC'
        transfer_amount = '0.51'
        transfer_type = 'master-transfer-out'
        tid = self.api.subs_transfer(sub_id, currency, transfer_amount, transfer_type);
        print(tid)

    def test_sub_transfer_record(self):
        sub_id = 'CA648855702269333504'
        ava = self.api.subs_transfer_record(sub_id)
        print(ava)
