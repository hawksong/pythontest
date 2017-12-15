'''
Created on 2017年12月15日

@author: user
'''
import json

# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    "name": 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])