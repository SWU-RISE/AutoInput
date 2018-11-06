# -*- coding: utf-8 -*-

import random

from random import randint
import string

class  RandChar(object):
    def __init__(self, a=-1, b=-1):
        self.low=a
        self.high=b

    def nextElem(self):
        if type(self.low) ==type(1) and self.low==-1: # all char
            return str(random.randint(string.ascii_letters))
        if type(self.low) ==type(1) and self.low==-2:   # all lower  char
            return str(random.randint(string.ascii_lowercase))
        if type(self.low) ==type(1) and self.low==-3:  # all upper  char
            return str(random.randint(string.ascii_uppercase))
        if type(self.high) ==type(1) and  self.high==-1: # one char in set
            return str(random.choice(self.low))
        else:
            return str(chr(random.randint(ord(self.low), ord(self.high))))



class RandInt(object):
    def __init__(self, a=0, b=0):
        self.low=a
        self.high=b
    def nextElem(self):
        if self.low==0 and self.high==0:
            return random.randint(0,200)
        elif self.low> self.high:
            return random.randint(-200,0)
        else:
            return random.randint(self.low, self.high)
