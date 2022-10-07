import json

import hw_06_06

with open("hw06.json","r") as rd:
   baza=json.load(rd)

def get_keys(d, keys):
   for k, v in d.items():

      if k == keys:
         print(keys,[d[k]])

      if isinstance(v, dict):
            get_keys(v, keys)




get_keys(baza, "title")
