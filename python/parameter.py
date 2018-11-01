# -*- coding: utf-8 -*-

class Parameter(object):
    def __init__(self, input, name  ):
        
        self.name=name
        self.t="integer"
        self.low=0
        self.sup=10000
        self.charRand=

    def nextElem(self):
        if self.t=="letter":
            
            return randchar(self.low, self.sup)
        elif self.t=="integer":
            return randint(self.low, self.sup)
        else:
            random.uniform(self.low, self.sup)
