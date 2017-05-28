"""
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]

# 期待输出: ['hello', 'world', 'apple']
print(L2)

"""

L1 = ['Hello','World',18,'Apple',None]

L2 = [x.lower() for x in L1 if isinstance(x,str) == True]

print(L2)