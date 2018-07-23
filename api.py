from flask import g
from urllib import parse, request
from flask_httpauth import HTTPBasicAuth
import json
from tool import config_para

app_key = '63aa11e5aea0a71c'


auth = HTTPBasicAuth()

# @auth.verify_password
# def verufy_password(email, password):
#     if email == '':
#         # g.current_user = AnonymousUser()

def send_request(content):

    url = 'http://openapi.youdao.com/api'
    textmod = {'q': content, 'from': 'auto', 'to': 'auto', 'appKey': app_key,
               'salt': '1', 'sign': config_para(content, '1')}
    textmod = parse.urlencode(textmod)
    print(textmod)
    req = request.Request(url='%s%s%s' % (url, '?', textmod))
    res = request.urlopen(req)
    res = res.read()

    result = json.loads(res.decode(encoding='utf-8'))

    print(result['translation'])

    # return result.get('translation', default=None)
    return result['translation']