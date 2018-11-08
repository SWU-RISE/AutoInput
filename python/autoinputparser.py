# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import mechanize
from nltk.book import FreqDist
from bs4 import BeautifulSoup
from html2text import html2text 
import psycopg2, random
from casestruct  import *

from randvalue import *
from nlputil import *
import codecs

BLOCK_TYPE=["line", "case", "file"]
VALUE_TYPE=["integer", "number", "letter" ]

DOMAIN_ADJ=["positive","lowercase" ]
LOCATION=["first", "end", "last"  ]
FOR_WORD=["each", "every" ]

class Input(object):

    def __init__(self, html_text):
        soup = BeautifulSoup(html_text,'lxml')
        self.raw=soup.get_text();
        self.sents=nltk.sent_tokenize(self.raw)


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
                
        print( self.num_words)


        possible_parameter_name=set([ w for w in self.tokens if len(w)==1 and w.isalpha()])

        self.param=[]
        for p in possible_parameter_name:
            if isParameter(self.text, p):
                self.param.append(Parameter(self, p))
                
        print( "contain:")
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


def connectDatabase():
    try:
        conn = psycopg2.connect(database = "onlinejudge", user = "onlinejudge", password = "onlinejudge", host = "47.95.215.87", port = "5111")
        cur=conn.cursor() 
    except:
        print( "I am unable to connect to the database")
        print( "Opened database successfully")
        
        cur.close()
        conn.close()
        return (False, False)
    return (conn, cur)
        

def findAllBlockWords():
    return findAllSimilarWords(BLOCK_TYPE)


def getAllInputTofile(f):

    （conn, cur)=connectDatabase()
    if !conn:
        return
    

    try:
       cur.execute("""SELECT _id, input_description from problem""")
    except:
        print( "I can't search in the database")
        cur.close()
        conn.close()
        return 

    f=open(f,"w")
    rows=cur.fetchall()
    for row in rows:
        soup = BeautifulSoup(row[1],'lxml')
        raw=soup.get_text();
        f.write(raw)
        f.write("\n")

        
    cur.close()
    conn.close()
    
    f.close()
    
def getFirstLine(f):
    （conn, cur)=connectDatabase()
    
    if !conn:
        return

    try:
       cur.execute("""SELECT _id, input_description from problem""")
    except:
        print( "I can't search in the database")
        cur.close()
        conn.close()
        return

    f=open(f,"w")    
    rows=cur.fetchall()
    for row in rows:
        soup = BeautifulSoup(row[1],'lxml')
        raw=soup.get_text();
        sents=nltk.sent_tokenize(raw)
        if len(sents)>0:
            f.write(sents[0])
            f.write("\n")
        
    cur.close()
    conn.close()
    f.close()


def getLastLine(f):
    （conn, cur)=connectDatabase()
    if !conn:
        return

    try:
       cur.execute("""SELECT _id, input_description from problem""")
    except:
        print( "I can't search in the database")
        cur.close()
        conn.close()
        return

    f=open(f,"w")    
    rows=cur.fetchall()
    for row in rows:
        soup = BeautifulSoup(row[1],'lxml')
        raw=soup.get_text();
        sents=nltk.sent_tokenize(raw)
        if len(sents)>0:
            f.write(sents[0])
            f.write("\n")
        
    cur.close()
    conn.close()
    f.close()
    
def getNltkText(f):
    fo=open("f")
    raw=fo.read()
    fo.close()
    raw = raw.decode('utf8')
    tokens = word_tokenize(raw)
    return nltk.Text(tokens)
    

if __name__=="__main__":
    # print(findAllBlockWords())
    # exit(0)
    
    # t=Test_case()
    # print( t.nextElem())
    # exit(0)
    
#    for i in  range(10):
#        print( RandChar('a','h'))

    getAllInputTofile("data/allinput.txt")
    getFirstLine("data/allFirstLine.txt")
    getLastLine("data/allLastLine.txt")
    
    
        
    fo=open("data/data.txt")

    raw=fo.read()
    fo.close()
    raw = raw.decode('utf8')
    tokens = word_tokenize(raw)
    text = nltk.Text(tokens)
    print("similar n")
    print (text.similar("n"))
    print("similar integer")
    print (text.similar("integer"))
    print("similar greater")
    print (text.similar("greater"))
    print("similar one")
    print (text.similar("one"))
    exit(0)
    
    
    tokens=nltk.word_tokenize(text)
    text=nltk.Text(tokens)
    text.similar("n")
    exit(1)
        
    inputs={}
    
    for row in rows:
        inputs[row[0]]=Input(row[1])
        
