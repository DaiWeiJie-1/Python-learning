"""
斐波那契數列
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1

fib(6)

#当执行到yield的时候直接跳出循环并返回yield，当再调用next时,从上次终端的yield处继续执行
def fib_yield(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n +1
    
f = fib_yield(6)
print(next(f))