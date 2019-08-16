import requests
from novadax.exception import *
from novadax.impl.http_auth import HTTPAuth


class HTTPClient(object):
    def __init__(self, url, access_key = None, secret_key = None):
        self._url = url
        if access_key and secret_key:
            self._auth = HTTPAuth(access_key, secret_key)
        else:
            self._auth = None

    def get(self, path, params = dict()):
        return self._request(False, 'get', path, params = params)

    def post(self, path, params = dict(), json = dict()):
        return self._request(False, 'post', path, params = params, json = json)

    def get_with_auth(self, path, params = dict()):
        return self._request(True, 'get', path, params = params)

    def post_with_auth(self, path, params = dict(), json = dict()):
        return self._request(True, 'post', path, params = params, json = json)

    def _request(self, auth, method, path, **kwargs):
        url = self._url + path
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

    def _filter_none(self, data):
        if isinstance(data, dict):
            return { k: v for k,v in data.items() if v is not None }
        return data