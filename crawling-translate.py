# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:48:10 2019

@author: Ecole
"""
import json
import urllib.request
import urllib.parse

content = input('please input the words neend to translate:')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}

data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15551183006576'
data['sign'] = '19dba145a9409826b0848bd31fea0a5d'
data['ts'] = '1555118300657'
data['bv'] = 'ab57a166e6a56368c9f95952de6192b5'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY-REALTIME'

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)
print('翻译的结果是：%s' %  (target['translateResult'][0][0]['tgt']))