'''
Created on 2017年12月14日

@author: user
'''
array = [9,2,7,4,5,6,3,8,1,10]       
L = len(array)
for i in range(L):
    for j in range(L-i):
        if array[L-j-1]<array[L-j-2]:
            array[L-j-1],array[L-j-2]=array[L-j-2],array[L-j-1]
for i in range(L):
    print (array[i])