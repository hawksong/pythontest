'''
Created on 2017年12月14日

@author: user
'''
def prime_sieve(n):
    flags = [True] * n
    flags[0] = flags[1] = False
    for i in range(2, n):
        if flags[i]:
            yield i
            for j in range(2, int((n - 1) / i) + 1):
                flags[i * j] = False

for p in prime_sieve(100):
    print (p)