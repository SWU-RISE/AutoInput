# -*- coding: utf-8 -*-

class Head(object):
    def __str__(self):
        return ""
    def getBodyLoopNum(self):
        return [0]
    def nextElem(self):
        pass

    
class HeadOne(Head):
    def __init__(self, RN):
        self.sep=" "
        self.RN=[RN]
        self.nextElem()
        
    def __str__(self):
        return self.sep.join([str(d) for d in self.loop ])+"\n"

    
    def getBodyLoopNum(self):
        return self.loop
    
    def nextElem(self):
        self.loop=[r.nextElem for r in self.RN ]

        
class HeadMore(Head):
    def __init__(self, rns, sep=" "):
        self.sep=sep
        self.RNs=rns
        self.nextElem()
        
    
class Tail(object):
    def __init__(self,line=""):
        self.line=line
    def __str__(self):
        return self.line
 
    
class Test_case(object):
    def __init__(self,  head=Head(), tail=Tail(), body=None, sep=" "):
        self.isNest=False
        self.head=head
        self.bofy=body
        self.tail=tail
        self.sep=sep
        self.lineNum=RandInt(4,10)
        self.num=RandInt(3,6)
        self.Data=RandInt()
    def  getLineNum(self):
        return self.lineNum.nextElem()
        
    def lineElemNum(self, i):
        return self.num.nextElem()

    def lineEndStr(self):
        return ""
    
    def headStr(self):
        return  str(self.head)
    
    def tailStr(self):
        return str(self.tail)
    
    def nextData(self):
        return str(self.Data.nextElem())
    
    def getSep(self):
        return self.sep
    
    def nextElem(self):
        if self.isNest:
            dummy=str(self.head)
            n=self.head.getBodyLoopNum()
            for i in n:
                dummy+=self.body.nextOne(self.head,i)
                dummy+=self.tail.end(n)
                return dummy
        else:
            m=self.getLineNum()
            dummy=str(self.head)
            for i in range(m):
                if i>0 :
                    dummy+="\n"
                k=self.lineElemNum(i)
                for j in range(k):
                    if j>0:
                        dummy+=self.getSep()
                    dummy+=self.nextData()
                dummy+=self.lineEndStr()
            return dummy+str(self.tail)
