def sliceList(list,n):
    #从0取到N
    result = list[0:n]
    print(result)


L = ['1','2','3','4','5']
sliceList(L,3)


##################################

L1 = list(range(10))
print(L1)

#从首位取到2
print(L1[:2])

#从倒数第五个取到倒数diere
print(L1[-5:-2])

#前7个数每隔两个取一个
print(L1[:7:2])


L2 = ('a','b','c','d','e')

print(L2[:3])