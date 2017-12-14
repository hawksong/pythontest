'''
Created on 2017年12月14日

@author: user
'''
"""
def grep(pattern):
    print ("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print (line)
if __name__ == '__main__':
    g = grep("python")
    next(g)
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
            
"""

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
        
for i in fib():
    print(i)