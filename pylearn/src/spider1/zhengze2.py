'''
Created on 2017年12月12日

@author: user
'''
'''
import re
 
line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, flags=re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
'''