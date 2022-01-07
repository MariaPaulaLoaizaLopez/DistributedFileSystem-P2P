import string
import random
import hashlib
import os


class Range:
    def __init__(self,lb,ub):
        self.lb = lb
        self.ub = ub

    def isFirst(self):
        return self.lb > self.ub

    def member(self,id):
        if self.isFirst():
            return (id > self.lb and id <= 1<<160) or (id >= 0 and id <= self.ub)

        else:
            return id > self.lb and id <= self.ub

    def toStr(self):
        if self.isFirst():
            return '(' + str(self.lb) + ' , 2^160) U [' + '0 , ' + str(self.ub) + ']'

        else:
            return '(' + str(self.lb) + ' , '+ str(self.ub) + ']'

