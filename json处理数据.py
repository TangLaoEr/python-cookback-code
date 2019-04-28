#import json
#
#d = {
#    'a':True,
#    'b':'Hello',
#    'c':None
#}
#
#print(json.dumps(d))


# 序列化一个对象
import json

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(2,3)

def serialize_instance(obj):
    d = {'__classname__':type(obj).__name__}
    d.update(vars(obj))
    return d

dums_data = json.dumps(p,default=serialize_instance)



def unserialize_instance(d):
    """反序列化"""
    classname = d.pop('__classname__',None)
    if classname:
        """创建对象"""
        # obj = eval('classname()')
        file = __import__(__name__)
        ClassName = getattr(file,classname)
        obj = ClassName.__new__(ClassName)
        for key,value in d.items():
            setattr(obj,key,value)
        return obj.__dict__




print(json.loads(dums_data,object_hook=unserialize_instance))
