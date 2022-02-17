#!/usr/bin/env python
# coding: utf8

import urllib
import urllib2
import json

url = 'http://ccpl.psych.ac.cn/textmind/analysis'  
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76' #将user_agent写入头信息  
#txt = {'str' : '红色发财果仿真花冬青假花插花摆设客厅家居新年装饰婚庆花艺摆件 漂亮美丽 优美 芬芳'}  #post数据  
headers = { 'User-Agent' : user_agent }  


def pred(txt):
    data = urllib.urlencode(txt)                   #对post数据进行url编码  
    req = urllib2.Request(url, data, headers)  
    response = urllib2.urlopen(req)  
    the_page = response.read() 
    data = json.loads(the_page)
    return data["result"][52]["value"]
