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
        print f





def isParameter(text, w ):
    print w
    try:
        f=text.findall(r"<\d+>(<.*>)<"+w+"> (<.*>)<\d+>")
    except:
        return False
    
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
    
