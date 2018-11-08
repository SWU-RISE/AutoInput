# -*- coding: utf-8 -*-

from randvalue import *
import random


class Parameter(object):
    def __init__(self,  name  ):
        
        self.name=name
        self.t="integer"
        self.low=0
        self.sup=10000

    def nextElem(self):
        if self.t=="letter":
            return RandChar(self.low, self.sup)
        elif self.t=="integer":
            return RandInt(self.low, self.sup)
        else:
            random.uniform(self.low, self.sup)
            
    def __str__(self):
        return str(name)
