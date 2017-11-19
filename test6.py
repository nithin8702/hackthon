# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:31:41 2017

@author: Admin
"""


import requests
import pandas as pd
import json


a_url = 'http://127.0.0.1:5002/employees'

#r = requests.get(a_url)
#data = json.loads(r.text)

#for items in data:
#    print(str(items['id']) + ' ' + items['name'])
    
#data = {"val" : "24.3"}
#data_json = json.dumps(data)
dsMapping = pd.read_csv('datasetmapping.csv')
ds1 = pd.read_csv('ds1.csv')
ds2 = pd.read_csv('ds2.csv')
data={'ds1':ds1.to_json(),'ds2':ds2.to_json(),'dsMapping':dsMapping.to_json()}
#data_json = data.to_json()
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}

response = requests.post(a_url, data=data_json)

#from pydoc import locate
#my_class = locate('G:\DataScience\Samples\Demo1\test7.test.greet')
#print(my_class('nithin'))

import importlib.util
#import sys, inspect
spec = importlib.util.spec_from_file_location("dynamicfunction", "G:\\DataScience\\Samples\\Demo1\\test7.py")
cls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cls)


#dir(cls)
#clsmembers = inspect.getmembers(cls, inspect.isclass)
#clsmembers[0][0]
#getattr(cls.test, 'greet')
getattr(cls,clsmembers[0][0]).greet('s')
getattr(cls,clsmembers[0][0])['greet']
a2 = getattr(cls,clsmembers[0][0])
a2.greet('ddd')

a2['greet']('dd')

a1 = inspect.getmembers(clsmembers, inspect.isclass)



cls.test.match(123,123)
cls.test.greet('nithin')
cls['test'].greet('nithin')
#foo.test.match(123,123)

