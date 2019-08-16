from time import time
from urllib.parse import urlparse, parse_qsl, quote
from requests.auth import AuthBase
from novadax.impl import utils

class HTTPAuth(AuthBase):
    _without_content_body_method = ['GET', 'DELETE', 'HEAD']

    def __init__(self, access_key, secret_key):
        self._access_key = access_key
        self._secret_key = secret_key

    def __call__(self, r):
        timestamp = self._get_timestmap()
        r.headers['X-Nova-Access-Key'] = self._access_key
        r.headers['X-Nova-Signature'] = self._get_signature(r.method, r.url, r.body, timestamp)
        r.headers['X-Nova-Timestamp'] = timestamp
        return r

    def _get_timestmap(self):
        return int(time() * 1000)

    def _get_signature(self, method, url, body, timestamp):
        signature_str = self._get_signature_str(method, url, body, timestamp)
        return utils.hmac_sha256_hex(self._secret_key, signature_str)

    def _get_signature_str(self, method, url, body, timestamp):
        url_parsed = urlparse(url)
        path = url_parsed.path
        params = self._get_sorted_query_params(url_parsed.query)

        if method not in self._without_content_body_method:
            content_md5 = utils.md5_hex(body.decode('UTF-8'))
            return '{}\n{}\n{}\n{}'.format(method, path, content_md5, timestamp)
        else:
            return '{}\n{}\n{}\n{}'.format(method, path, params, timestamp)

    def _get_sorted_query_params(self, query):
        query_dict = dict(parse_qsl(query))
        sorted_query_item = sorted(query_dict.items(), key=lambda x: x[0], reverse=False)
        sorted_query = map(lambda x: '{}={}'.format(quote(x[0]), quote(x[1])), sorted_query_item)
        return '&'.join(sorted_query)
