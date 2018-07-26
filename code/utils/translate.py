#!/usr/bin/env python3
#--coding:utf-8--
"""
translate.py
2018-07-26: 百度翻译接口
"""


#sys
import http.client
import hashlib
from urllib import parse
import random

#3rd
import pronto
import pandas as pd

#global setting
baiduAppid = ""
baiduSecretKey = ""


def baiduTranslate(q,fromLang="en",toLang="zh"):
    myurl = '/api/trans/vip/translate'
    httpClient = None
    salt = random.randint(32768, 65536)
    sign = baiduAppid+q+str(salt)+baiduSecretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+baiduAppid+'&q='+parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        ts = response.read().decode('utf-8')
        ts = eval(ts)
        rs = ""
        for line in ts['trans_result']:
            rs += line['dst']+'\n'
        return rs
    except Exception as e:
        print(e)
        return None
    finally:
        if httpClient:
            httpClient.close()    
    


print(baiduTranslate("I love Python and computational biology! HA-HA-a~"))
