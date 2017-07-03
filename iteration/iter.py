d = {'a':1,'b':2,'c':3,'d':4}

#iterate key
for key in d:
    print(key)


#iterate value
for value in d.values():
    print(value)


#iterate key and value
for k,v in d.items():
    print("key  = %s,value  = %s " %(k,v))


#判断是否是可迭代对象
from collections import Iterable
result = isinstance('abc',Iterable)

print(result)