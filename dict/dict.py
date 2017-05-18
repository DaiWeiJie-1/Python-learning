d = {'a':1, 'b':2, 'c':3}
print(d['a'])

print("get " + str(d.get('aa',-1)))

d.pop('a')
print(d)

help(abs)