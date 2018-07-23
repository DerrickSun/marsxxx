# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, request, url_for
from api import send_request
import json


base_url = 'http://127.0.0.1:5000123321'

app_key = '63aa11e5aea0a71c'

key = 'tchbOHrzh4dJJ0xPmbmXc3OlRJEXUOZN'

app = Flask(__name__)

data = [
      {
        'id': '1',
        'image': 'http://img1.huiyijingling.cn/UploadImage/Meet/20161010/4ntia7d5/636117184529372567.png',
        'title': '对话产品总监 | 深圳·北京PM大会 【深度对话小米/京东/1号店/百度等产品总监】',
        'num': '304',
        'state': '进行中',
        'time': '10月09日 17:59',
        'address': '深圳市·南山区'
      },
      {
        'id': '1',
        'image': 'http://img1.huiyijingling.cn/UploadImage/Meet/20161010/4ntia7d5/636117184835348263.png',
        'title': 'AI WORLD 2016世界人工智能大会',
        'num': '380',
        'state': '已结束',
        'time': '10月09日 17:39',
        'address': '北京市·朝阳区'
      },
      {
        'id': '1',
        'image': 'http://img1.huiyijingling.cn/UploadImage/Meet/20161010/4ntia7d5/636117186019220383.png',
        'title': 'H100太空商业大会',
        'num': '500',
        'state': '进行中',
        'time': '10月09日 17:31',
        'address': '大连市'
      },
      {
        'id': '1',
        'image': 'http://img1.huiyijingling.cn/UploadImage/Meet/20161010/4ntia7d5/636117185105463337.png',
        'title': '【报名】年度盛事，大咖云集！2016凤凰国际论坛邀您“与世界对话”',
        'num': '150',
        'state': '已结束',
        'time': '10月09日 17:21',
        'address': '北京市·朝阳区'
      },
      {
        'id': '1',
        'image': 'http://img1.huiyijingling.cn/UploadImage/Meet/20161010/4ntia7d5/636117185186696080.png',
        'title': '新质生活 · 品质时代 2016消费升级创新大会',
        'num': '217',
        'state': '进行中',
        'time': '10月09日 16:59',
        'address': '北京市·朝阳区'
      }
]




@app.route('/api/translate', methods=['GET'])
def translate():
    text = request.args.get('text')
    content = send_request(text)

    return jsonify({'content': content})


@app.route('/api/translate/<string:text>', methods=['GET'])
def translateContent(text):
    content = send_request(text)
    # return jsonify({'content': content})
    var = '.'.join(content)

    return var
    # return %s % content


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/list', methods=['GET'])
def get_list():
    result = json.dumps(data)
    return result


@app.route('/api/piclist', methods=['GET'])
def get_imageslist():
    images = [
        {
            'id': 1,
            'title': 'Buy groceries',
            'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
            # 'url': url_for('static', filename='pic/1.jpg', _external=True)
            'url': base_url + '/static/pic/3.jpg'

        },
        {
            'id': 2,
            'title': 'Learn Python',
            'description': 'Need to find a good Python tutorial on the web',
            # 'url': url_for('static', filename='pic/2.jpg', _external=True)
            'url': base_url + '/static/pic/3.jpg'
        },
        {
            'id': 3,
            'title': 'play Python',
            'description': 'Need to find a good Python tutorial on the web',
            # 'url': url_for('static', filename='pic/3.jpg', _external=True)
            'url': base_url + '/static/pic/3.jpg'
        }
    ]
    result = json.dumps(images)
    return result


if __name__ == '__main__':
    # app.run(debug=True)

    app.run(host='10.3.30.72', port=5000)
