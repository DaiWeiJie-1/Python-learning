from functools import reduce

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

# str也是可以遍历的
char = map(char2num,'43134')




def fn(x,y):
    return x * 10 + y

i = reduce(fn,char)
print(i)
