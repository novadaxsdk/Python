from requests.auth import AuthBase

from novadax.kernel.encryptor import Encryptor


class BaseHTTPAuth(AuthBase, Encryptor):
    _without_content_body_method = ['GET', 'DELETE', 'HEAD']

    def __init__(self, access_key, secret_key):
        Encryptor.__init__(self, access_key, secret_key)

    def __call__(self, r):
        timestamp = self.get_timestamp()
        r.headers['X-Nova-Access-Key'] = self._access_key
        r.headers['X-Nova-Signature'] = self.get_signature(r.method, r.url, r.body, timestamp)
        r.headers['X-Nova-Timestamp'] = timestamp
        return r
