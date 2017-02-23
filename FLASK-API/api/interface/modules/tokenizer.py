from __future__ import print_function
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import io
import redis
from ngram import NGram
import nltk

def Split_Sentence(sentence):
    verb=sentence.split()
    array=[]
    for i in range(0,len(verb)):
        if i+1<len(verb):
            verbs = verb[i]+" "+verb[i+1]
            array.insert(i,verbs)

    return array

def HowMamyVerbinText2(text):
    hm=0

    text = Split_Sentence(text)
    print (text)
    for i in range(0,len(text)):
        for j in range(0,len(text)):
            if text[i]==text[j]:
                hm+=1
        r.set(text[i], hm)
        hm = 0

def HowMamyVerbinText(text):
    hm=0

    text = nltk.word_tokenize(text)
    print (text)
    for i in range(0,len(text)):

        for j in range(0,len(text)):

            if text[i]==text[j]:
                hm+=1
        r.set(text[i], hm)
        hm = 0



def FixedText(textt):
    Value=[0.5]
    a=0
    fix=""
    maxvalue=Value[0]
    for key in r.scan_iter():

        if NGram.compare(textt,key,N=1) >= 0.5:
            a=float(r.get(key))/10
            b=NGram.compare(textt,key)+float(a)

            if b>maxvalue:
                maxvalue=b
                fix=key
        else:
            continue
    textt=fix
    print (a)
    return  textt


r = redis.StrictRedis()






#textt="waz"
#FixedText(textt)
#print (a)

FixedText(str_read)
