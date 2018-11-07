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


BLOCK_TYPE=["line", "case", "file"]
VALUE_TYPE=["integer", "number", "letter" ]

DOMAIN_ADJ=["positive","lowercase" ]
LOCATION=["first", "end", "last"  ]
FOR_WORD=["each", "every" ]

class Input(object):

    def __init__(self, html_text):
        print(html_text)
        soup = BeautifulSoup(html_text,'lxml')
        self.raw=soup.get_text();
        self.sents=nltk.sent_tokenize(self.raw)
        #print( "sentences:")
        #pprint.pprint(self.sents)
        #print ("End sentences.")

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



if __name__=="__main__":
    # t=Test_case()
    # print( t.nextElem())
    # exit(0)
    
#    for i in  range(10):
#        print( RandChar('a','h'))
        
    try:
        conn = psycopg2.connect(database = "onlinejudge", user = "onlinejudge", password = "onlinejudge", host = "47.95.215.87", port = "5111")
        cur=conn.cursor() 
    except:
        print( "I am unable to connect to the database")
        print( "Opened database successfully")

    try:
       cur.execute("""SELECT _id, input_description from problem""")
    except:
        print( "I can't search in the database")


    rows=cur.fetchall()
    inputs={}
    
    for row in rows:
        inputs[row[0]]=Input(row[1])
        
