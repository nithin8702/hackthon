# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:22:50 2017

@author: Admin
"""

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import json
import pandas as pd
import importlib.util


app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):        
        return list([{'id':1,'name':'user 1'},{'id':2,'name':'user 2'}])
    def post(self):
        print('posts started')
        data_json = json.loads(request.data)
#        print('data_json.ds1',data_json['ds1'])
#        print('data_json.ds2',data_json['ds2'])
#        print('data_json.dsMapping',data_json['dsMapping'])
        
        
#        spec = importlib.util.spec_from_file_location("dynamicfunction", "G:\\DataScience\\Samples\\Demo1\\test7.py")
#        foo = importlib.util.module_from_spec(spec)
#        spec.loader.exec_module(foo)
#        foo.test.match('nithin')


        
        
        dsMapping = pd.read_json(data_json['dsMapping'])
        ds1 = pd.read_json(data_json['ds1'])
        ds2 = pd.read_json(data_json['ds2'])
#        print(dsMapping)
#        ds=zip(ds1,ds2)
#        print(ds)
        
        for i, row in dsMapping.iterrows():
#            print('row id \n',row)
#            print('dataset1 is \n',row['dataset1'])
#            print('row starts : ' + str(i))
#            print('ds1[row.dataset1]\n',ds1[row.dataset1].iloc[i])
            
            spec = importlib.util.spec_from_file_location("dynamicfunction", "G:\\DataScience\\Samples\\Demo1\\test7.py")
            cls = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cls)
            
            d1 = ds1[row['dataset1']]
            d2 = ds2[row['dataset2']]
            ds = list(zip(d1,d2))
#            print(ds)
            for d in ds:
                print(str(d[0]) + ' - ' + str(d[1]))
#            print(d1.size)
            
#            print('d2',d2)
#           print('ds1[row.dataset1]\n',ds1[row.dataset1])
#            for d1 in ds1[row.dataset1]:
#                print(d1.iloc[i])
#            print('ds2[row.dataset2]\n',ds2[row.dataset2])
#            print(row.dataset1)
#            print(row.dataset2)
#            print(i)
        
        
#        print('\ndsMapping')
#        print(dsMapping)
#        print('\nds1')
#        print(ds1)
#        print('\nds2')
#        print(ds2)
        
        
#        print(ds1)
#        ds = pd.DataFrame(data=data_json['dsMapping'])
#        print(ds)
#        ds1Mapping = data_json['dsMapping'].dataset1
#        ds2Mapping = data_json['dsMapping']['dataset2']
#        ds1 = pd.DataFrame(data_json['ds1'])
#        ds2 = pd.DataFrame(data_json['ds2'])
#        print(ds1)
#        tmp = pd.DataFrame(data_json)
#        print(tmp)
    
api.add_resource(Employees, '/employees') # Route_1

if __name__ == '__main__':
     app.run(port='5002')