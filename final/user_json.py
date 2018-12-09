'''
Created on Dec 7, 2018

@author: USER
'''
import json 

data = {}
data['user_1'] = []
data['user_1'].append(['duy','123'])
data['user_2'] = []
data['user_2'].append(['huy','456'])
data['user_3'] = []
data['user_3'].append(['thach','789'])

f = open('user.json','w')
json.dump(data,f)
