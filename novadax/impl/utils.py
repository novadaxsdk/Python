import hmac
import hashlib
import base64

def hmac_sha256_hex(key, text):
    return hmac.new(bytes(key, 'UTF-8'), bytes(text, 'UTF-8'), hashlib.sha256).hexdigest()

def md5_hex(text):
    obj = hashlib.md5()
    obj.update(bytes(text, 'UTF-8'))
    return obj.hexdigest()
