from student import *
import json

s = Student('dwj',12,23)
# default 对应Student中的一个方法，方法定义了dict的转化
print(json.dumps(s,default=Student.student2dict))


#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s,default=lambda obj:obj.__dict__))


