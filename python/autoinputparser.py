#!/usr/bin/python
from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import mechanize
from nltk.book import FreqDist
from bs4 import BeautifulSoup
from html2text import html2text 
import psycopg2, random
from random import randint
import string



BLOCK_TYPE=["line", "case", "file"]
VALUE_TYPE=["integer", "number", "letter" ]

DOMAIN_ADJ=["positive","lowercase" ]
LOCATION=["first", "end", "last"  ]
FOR_WORD=["each", "every" ]


def randchar(a=-1, b=-1):
    if a==-1:
        str(random.randint(string.ascii_lowercase))
    if b==-1:
        str(random.choice(a))
    else:
        return str(chr(random.randint(ord(a), ord(b))))


class Head(object):
    def __str__(self):
        return ""
    def getBodyLoopNum(self):
        return 0
    def nextElem(self):
        a=1
    
class HeadOne(Head):
    def __init__(self, RN):
        self.RN=RN
        self.loop=RN.nextElem();
        
    def __str__(self):
        return str(self.loop)
    
    def getBodyLoopNum(self):
        return self.loop
    
    def nextElem(self):
        self.loop=self.RN.next()

        

class Tail(object):
    def __init__(self,line=""):
        self.line=line
    
    def end(self, n):
        return self.line

    
class Test_case(object):
    def __init__(self,  body, head=None, tail=None, sep=" "):
        self.isNest=False
        self.head=head
        self.bofy=body
        self.tail=tail
        self.sep=sep

    def lineElemNum(self,head, n):
        return randint(4,10)
    
    def head(self):
        return ""
    
    def tail(self):
        return ""
    
    def nextElem(self):
        return str(randint(4,10))
    
    def getSep(self):
        return self.sep
    
    def nextOne(self):
        if self.isNest:
            dummy=str(self.head)
            n=self.head.getBodyLoopNum()
            for i in n:
                dummy+=self.body.nextOne(self.head,i)
                dummy+=self.tail.end(n)
                return dummy
        else:
            m=self.lineElemNum()
            dummy=self.head()
            for i in range(m):
                if i>0:
                    dummy+=self.getSep()
                dummy+=self.nextElem()
            return dummy+self.tail()

        
class IndexedText(object):

    def __init__ (self, stemm, text):
        self._text=text
        self._stemmer=stemm
        self._index=nltk.Index((self._stem(word.lower()), i) for
                               (i, word) in enumerate(text))
    def index(self, word):
         key = self._stem(word)
         if key in self_index:
             return self_index[key]
         else:
             return []

    def _stem(self, word):
        return self._stemmer.stem(word).lower()
    

    
class Parameter(object):
    def __init__(self, input, name  ):
        
        self.name=name
        self.t="integer"
        self.low=0
        self.sup=10000

    def next_elm(self):
        if self.t=="letter":
            return randchar(self.low, self.sup)
        elif self.t=="integer":
            return randint(self.low, self.sup)
        else:
            random.uniform(self.low, self.sup)

            

def contain(text):
    f=text.findall(r"<contains> <\d+>")
    if f:
        print f

def isParameter(text, w ):
    print w
    f=text.findall(r"<\d+><.*><"+w+"> <.*><\d+>")
    if f:
        return True
    f=text.findall(r"<"+w+"> <.*><\d+>")
    if f:
        print f
        return True

    f=text.findall(r"<\d+><.*><"+w+">")
    if f:
        print f
        return True
    f=text.findall(r"<"+w+"><is><.*>{,2}<integer>")
    if f:
        print f
        return True
    

class Input(object):

    def __init__(self, html_text):
        soup = BeautifulSoup(html_text)
        self.raw=soup.get_text();
        self.sents=nltk.sent_tokenize(self.raw)
        print "sentences:"
        pprint.pprint(self.sents)
        print "End sentences."

        self.tokens=nltk.word_tokenize(self.raw)
        self.text=nltk.Text(self.tokens)
        self.lower_tokens=[w.lower() for w in self.tokens ]
        porter=nltk.PorterStemmer()
        self.index=IndexedText(porter, self.tokens)
        
        self.tags=nltk.pos_tag(self.tokens)
        self.num_words=[] #CD cardinal numeral, e.g. 1,2,3 one two three
        for (word, tag) in self.tags:
            if tag=="CD":
                self.num_words.append(word)
                
        print self.num_words


        possible_para_name=set([ w for w in self.tokens if len(w)==1 and w.isalpha()])

        self.param=[]
        for p in possible_para_name:
            if isParameter(self.text, p):
                self.param.append(Parameter(self, p))
                
        print "contain:"
        contain(self.text)
        
                
                
        """
        JJ adjective or numeral, ordinal
        third ill-mannered pre-war regrettable oiled calamitous first separable
        ectoplasmic battery-powered participatory fourth still-to-be-named
        multilingual multi-disciplinary ...
        ordinal numeral (first, 2nd)
        """
        self.order_words=[]
                

        self.com_words=[] #JJR  comparative adjective e.g. less, greater



if __name__=="__main__":
    for i in  range(10):
        print randchar('a','h')
        
    try:
        conn = psycopg2.connect(database = "onlinejudge", user = "onlinejudge", password = "onlinejudge", host = "47.95.215.87", port = "5111")
    except:
        print "I am unable to connect to the database"
    print "Opened database successfully"
    cur=conn.cursor()
    try:
        cur.execute("""SELECT _id, input_description from problem""")
    except:
        print "I can't search in the database"        


    rows=cur.fetchall()
    inputs={}
    
    for row in rows:
        inputs[row[0]]=Input(row[1])
        
