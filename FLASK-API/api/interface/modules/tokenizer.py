from __future__ import print_function
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
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
    f = open('database', 'a')
    hm=0

    text = Split_Sentence(text)
    print (text)
    for i in range(0,len(text)):
        for j in range(0,len(text)):
            if text[i]==text[j]:
                hm+=1
        print (text[i]+str(hm),file=f)
        hm=0

def HowMamyVerbinText(text):
    f = open('database', 'a')
    hm=0

    text = nltk.word_tokenize(text)
    print (text)
    for i in range(0,len(text)):
        for j in range(0,len(text)):
            if text[i]==text[j]:
                hm+=1
        print (text[i]+str(hm),file=f)
        hm=0

def FixedText(textt,database):
    Value=[0.5]
    #text=Split_Sentence(database)
    fix=""
    text = nltk.word_tokenize(database)
    maxvalue=Value[0]
    for i in range(0,len(text)):

        if NGram.compare(textt, text[i],N=1) > 0.5:
            b=NGram.compare(textt,text[i])+5

            if b>maxvalue:
                maxvalue=b
                fix=text[i]
    textt=fix
    return  textt
        
        
HowMamyVerbinText2("text to Tugay")
HowMamyVerbinText("text to text")
