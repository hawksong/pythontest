'''
Created on 2017年12月14日

@author: user
'''
class Person(object):  
    def __init__(self,name = '',age =10,sex='man'):  
        self.setName(name)  
        self.setAge(age)  
        self.setSex(sex)  
    def setName(self,name):  
        if not isinstance(name,str):  
            print ('name must be string')  
            return  
        self.__name = name  
    def setAge(self,age):  
        if not isinstance(age,int):  
            print(' age must be integer')  
            return  
        self.__age = age  
    def setSex(self,sex):  
        if sex !=  'man' and sex != 'woman':  
            print ('sex must be man or women')  
            return  
        self.__sex = sex  
    def show(self):  
        print ('name:',self.__name)  
        print ('age:',self.__age)  
        print ('sex:',self.__sex)  

class Teacher(Person):  
    def __init__(self,name = '',age = 30,sex = 'man',job= 'tutor'):  
        Person.__init__(self,name,age,sex)  
        self.setJob(job)  
    def setJob(self,job):  
        if not isinstance(job,str):  
            print ('job must be string')  
            return  
        self.__job = job  
    def show(self):  
        Person.show(self)  
        print('job:',self.__job)  
        
xiaoming=Person('xiaoming',30,'man')  
xiaoming.show()  

xiaohong = Teacher('xiaohong',40,'woman','math teacher')  
xiaohong.show() 