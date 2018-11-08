# -*- coding: utf-8 -*-

from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
import mechanize
from nltk.book import FreqDist
from bs4 import BeautifulSoup
from html2text import html2text 
import psycopg2, random


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


            

def contain(text):
    f=text.findall(r"<contains> <\d+>")
    if f:
        return True





def isParameter(text, w ):
    try:
        f=text.findall(r"<\d+>(<.*>)<"+w+"> (<.*>)<\d+>")
    except:
        return False
    
    if f:
        return True
    try:
        f=text.findall(r"<\d+>(<.*>)<.*><"+w+"><.*> (<.*>)<\d+>")
    except:
        return False
    
    if :
        return True
    try:
        f=text.findall(r"<"+w+"> <.*><\d+>")
    except:
        return False
    
    if f:
        return True

    f=text.findall(r"<\d+><.*><"+w+">")
    if f:
        return True
    f=text.findall(r"<"+w+"><is><.*>{,2}<integer>")
    if f:
        return True
    

def getAllPossible_parameter_name( tokens):
    """
    Obtaining all paramter name
    """
    possible_parameter_name=set([ w for w in tokens if len(w)==1 and w.isalpha()])
    
    parameters=[]
    text=nltk.Text(tokens)
    for p in possible_parameter_name:
        if isParameter(text, p):
            parameters.append(Parameter( p))
            
    return parameters

    
def findAllSimilarWords(words):
    re=[]
    f=open("data.txt")
    raw=f.read()
    f.close()
    raw=raw.decode('utf8')
    tokens=word_tokenize(raw)
    text=nltk.Text(tokens)
    for w in words:
        si=text.similar(w)
        re.append(si)
    return list(set(re))

def getAllCDNumber(raw):
    """
    #CD cardinal numeral, e.g. 1,2,3 one two three
    """
    tokens=nltk.word_tokenize(raw)
    text=nltk.Text(tokens)
    tags=nltk.pos_tag(tokens)
    CD_words=[] #CD cardinal numeral, e.g. 1,2,3 one two three
    for (word, tag) in tags:
        if tag=="CD":
            CD_words.append(word)
    return CD_words
