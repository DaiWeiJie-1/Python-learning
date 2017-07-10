from student import *
import json

#键值对一定要用""
json_str = '{"name":"dwj","age":12,"size":131}'
#通过student中定义的dict2student将dict转化成obj
print(json.loads(json_str,object_hook=Student.dict2student))