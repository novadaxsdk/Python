import requests

from novadax.exception import *
from novadax.kernel.http.base_http_auth import BaseHTTPAuth


class BaseHTTPClient:
    def __init__(self, endpoint, access_key=None, secret_key=None):
        self._endpoint = endpoint
        if access_key and secret_key:
            self._auth = BaseHTTPAuth(access_key, secret_key)
        else:
            self._auth = None

    def get(self, path, params=None):
        return self._request(False, 'get', path, params=params)

    def post(self, path, params=None, json=None):
        return self._request(False, 'post', path, params=params, json=json)

    def get_with_auth(self, path, params=None):
        return self._request(True, 'get', path, params=params)

    def post_with_auth(self, path, params=None, json=None):
        return self._request(True, 'post', path, params=params, json=json)

    def _request(self, auth, method, path, **kwargs):
        url = self._endpoint + path
        if auth and not self._auth:
            raise RuntimeException('A99999', 'access key and secret key is required.')
        elif auth:
            kwargs['auth'] = self._auth

        if 'params' in kwargs:
            if kwargs['params'] is None:
                del kwargs['params']
            else:
                kwargs['params'] = self._filter_none(kwargs['params'])

        if 'json' in kwargs:
            if kwargs['json'] is None:
                del kwargs['json']
            else:
                kwargs['json'] = self._filter_none(kwargs['json'])

        if 'timeout' not in kwargs:
            kwargs['timeout'] = 30

        try:
            r = requests.request(method, url, **kwargs)
        except requests.exceptions.RequestException as err:
            raise RuntimeException('A99999', str(err))

        result = r.json()

        if r.status_code >= 400:
            raise RequestException(result['code'], result['message'])
        return result

    @staticmethod
    def _filter_none(data):
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data
