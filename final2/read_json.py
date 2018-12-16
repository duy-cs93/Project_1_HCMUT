'''
Created on Dec 8, 2018

@author: USER
'''

import json 

def read_json():
    data_file = open("user.json",encoding = 'UTF-8')
    data = json.load(data_file)
    data_file.close()
    return data