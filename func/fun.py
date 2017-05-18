def abs(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError('bad type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad type')
    else:
        return (a+b)/2.0

print(abs(1, 2))
# print(abs("1", 4))






