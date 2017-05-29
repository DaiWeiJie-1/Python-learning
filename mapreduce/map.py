def f(x):
    return x * x

#map 针对list中的每个元素执行指定方法
r = map(f,[1,2,3,4,5,6,7])
print(list(r))