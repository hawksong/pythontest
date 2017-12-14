'''
Created on 2017年12月14日

@author: user
'''
from abc import ABCMeta, abstractmethod
class shape(object):  
    __metaclass__= ABCMeta
    def __init__(self):  
        self.color = 'black'  
    @abstractmethod  
    def draw(self):  
        pass  
class circle(shape):  
    def __init__(self,x,y,r):  
        self.x = x  
        self.y = y  
        self.r = r  
    def draw(self):  
        print('draw circle:(%d,%d,%d)'%(self.x,self.y,self.r))
        
        
class line(shape):  
    def __init__(self,x1,y1,x2,y2):  
        self.x1 = x1  
        self.y1 = y1  
        self.x2 = x2  
        self.y2 = y2  
    def draw(self):  
        print('draw circle:(%d,%d,%d,%d)'%(self.x1,self.y1,self.x2,self.y2))          

c=circle(1,2,3)  
c.draw()
l=line(1,2,3,4)
l.draw()
