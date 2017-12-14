'''
Created on 2017年12月14日

@author: user
'''
from decimal import Decimal

class Fees(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._fee = None
 
    #----------------------------------------------------------------------
    @property
    def fee(self):
        """
        The fee property - the getter
        """
        return self._fee
 
    #----------------------------------------------------------------------
    @fee.setter
    def fee(self, value):
        """
        The setter of the fee property
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value
 
#----------------------------------------------------------------------
f = Fees()
print(f.fee)
f.fee="1"
print(f.fee)
