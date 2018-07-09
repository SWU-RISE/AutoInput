#!/usr/bin/python
from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import mechanize
from nltk.book import FreqDist


from bs4 import BeautifulSoup
from html2text import html2text 


import psycopg2

BLOCK_TYPE=["line", "case", "file"]
VALUE_TYPE=["integer", "number", "letter" ]
DOMAIN_ADJ=["positive","lowercase" ]
LOCATION=["first", "end", "last"  ]
FOR_WORD=["each", "every" ]


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
    def __init__(self, lower_tokens, name ):
        self.name=name
        

        

class Input(object):

    def __init__(self, html_text):
        soup = BeautifulSoup(html_text)
        self.text=soup.get_text();

        self.tokens=nltk.word_tokenize(self.text)
        self.lower_tokens=[w.lower() for w in self.tokens ]
        porter=nltk.PorterStemmer()
        self.index=IndexedText(porter, self.tokens)
        
        self.tags=nltk.pos_tag(tokens)
        self.num_words=[] #CD cardinal numeral, e.g. 1,2,3 one two three
        for (word, tag) in self.tags:
            if tag=="CD":
                self.num_words.append(word)
        
                
    """
    JJ adjective or numeral, ordinal
    third ill-mannered pre-war regrettable oiled calamitous first separable
    ectoplasmic battery-powered participatory fourth still-to-be-named
    multilingual multi-disciplinary ...
    ordinal numeral (first, 2nd)
    """
        self.order_words=[]
        
        

        self.com_words=[] #JJR  comparative adjective e.g. less, greater
        

        
