'''
Created on 2017年12月12日

@author: user


'''


'''
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
'''

'''
birth = int(input('birth: '))

if birth < 2000:
    print('00前')
else:
    print('00后')
    
'''

'''
age=0
if age >= 18:
    pass
'''
    
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(3))
'''
'''
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
'''
'''
L =[m + n for m in 'ABC' for n in 'XYZ']
print(L)
'''
'''
g = (x * x for x in range(10))
print(g)
for n in g:
   print(n)
'''

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
