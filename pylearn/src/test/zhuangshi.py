'''
Created on 2017年12月14日

@author: user
'''
def a(fn):  
    print('a')  
  
    def d(st):  
        print(st+'d')  
    return d  
      
def b(fn):  
    print ('b') 
    return fn  
     
@a  
@b  
def c(st):  
    print(st)  
      
c('c')  
c('c') 