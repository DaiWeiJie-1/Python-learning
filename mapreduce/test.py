"""
1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""

def standard(s):
    #针对str进行切片处理
    return s[0].upper() + s[1:].lower()


s = map(standard,['adam', 'LISA', 'barT'])

print(list(s))



"""
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

"""
from functools import reduce
def pr(x,y):
    return x * y

def prod(list):
    return reduce(pr,list)

print(prod([3,5,7]))



"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
"""

from functools import reduce
def str2float(s):
    ss = s.split('.')
    if(len(ss) == 2):
        print(ss[0] + '; ' + ss[1])
        smallPos = len(ss[1])
        bignum = reduce(fn,map(char2int,ss[0]))
        smallnum = reduce(fn,map(char2int,ss[1]))
        print(str(bignum) + '; ' + str(smallnum/(10**smallPos)) + "; " + str(10**smallPos))
        return bignum + smallnum/(10**smallPos)
    return -1

def char2int(c):
    return {'0':0 , '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]


def fn(x,y):
    return x * 10 + y

a=str2float("123.456")
print(a)



