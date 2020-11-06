import hashlib
import hmac
from time import time
from urllib.parse import urlparse, parse_qsl, quote


class Encryptor:
    _without_content_body_method = ['GET', 'DELETE', 'HEAD']

    def __init__(self, access_key, secret_key):
        self._access_key = access_key
        self._secret_key = secret_key

    def get_access_key(self):
        return self._access_key

    def get_secret_key(self):
        return self._secret_key

    def get_signature(self, method, url, body, timestamp):
        signature_str = self.get_signature_str(method, url, body, timestamp)
        return self.hmac_sha256_hex(self._secret_key, signature_str)

    def get_signature_str(self, method, url, body, timestamp):
        url_parsed = urlparse(url)
        path = url_parsed.path
        params = self.get_sorted_query_params(url_parsed.query)

        if method not in self._without_content_body_method:
            content_md5 = self.md5_hex(body.decode('UTF-8'))
            return '{}\n{}\n{}\n{}'.format(method, path, content_md5, timestamp)
        else:
            return '{}\n{}\n{}\n{}'.format(method, path, params, timestamp)

    @staticmethod
    def get_timestamp():
        return int(time() * 1000)

    @staticmethod
    def get_sorted_query_params(query):
        query_dict = dict(parse_qsl(query))
        sorted_query_item = sorted(query_dict.items(), key=lambda x: x[0], reverse=False)
        sorted_query = map(lambda x: '{}={}'.format(quote(x[0]), quote(x[1])), sorted_query_item)
        return '&'.join(sorted_query)

    @staticmethod
    def hmac_sha256_hex(key, text):
        return hmac.new(bytes(key, 'UTF-8'), bytes(text, 'UTF-8'), hashlib.sha256).hexdigest()

    @staticmethod
    def md5_hex(text):
        obj = hashlib.md5()
        obj.update(bytes(text, 'UTF-8'))
        return obj.hexdigest()
