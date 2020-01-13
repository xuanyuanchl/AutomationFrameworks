import json
from builtins import staticmethod

class jsonParse(object):
    data:object = None
    
    def loadJson(self, file):
        fp = open(file)
        self.data = json.load(fp)
        return self.data
    
    def getValue(self, key):
        return self.data[key]
    
    def getDict(self, key):
        d = dict()
        d[key] = self.data[key]
        return d
    
    def pythonToJson(self, data:dict):
        return json.dumps(data)
    
    @staticmethod
    def cmp_dict(src_data,dst_data):   
        assert type(src_data) == type(dst_data),"type: '{}' != '{}'".format(type(src_data), type(dst_data))
        if isinstance(src_data,dict):
            assert len(src_data) == len(dst_data),"dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
            for key in src_data:                
                assert dst_data.has_key(key)    
                jsonParse.cmp_dict(src_data[key],dst_data[key])    
        elif isinstance(src_data,list):                  
            assert len(src_data) == len(dst_data),"list len: '{}' != '{}'".format(len(src_data), len(dst_data))    
            for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                jsonParse.cmp_dict(src_list, dst_list)
        else:
            assert src_data == dst_data,"value '{}' != '{}'".format(src_data, dst_data)
