import hashlib
from app import *

app_key = '63aa11e5aea0a71c'
key = 'tchbOHrzh4dJJ0xPmbmXc3OlRJEXUOZN'


def get_md5(string):

    hl = hashlib.md5()
    hl.update(string.encode(encoding='utf-8'))
    return hl.hexdigest()


def config_para(content, salt):

    result = app_key+content+salt+key
    return get_md5(result)
