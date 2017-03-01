#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from sklearn.feature_extraction.text import CountVectorizer
import json
from nltk import ngrams, re, pprint
from ngram import NGram
import pandas as pd
import redis

r_server=redis.Redis(host="redis",port=6379)
r_server.rpush("habale",0)
r_server.save
def get(paragraph):

    tokenized_data = nltk.word_tokenize(paragraph)
    return tokenized_data

text = """The Eurovision Song Contest has hit a major road bump, after 21 top level staff organising the event resigned.
The Ukrainian Eurovision team say they were stripped of major responsibilities in December, when a new boss was appointed to the organising committee.
According to their resignation letter, they were "completely blocked" from making decisions about the show.
The EBU, which founded Eurovision, told Ukraine's public broadcaster to "stick to the timeline" despite the upheaval.
It insisted the event would go ahead as planned in Kiev this May. Among the team members who resigned were two executive producers of this year's show.
All the staff were appointed by the Ukraine Public Broadcaster (UA:PBC), which is organising the contest after Ukrainian singer Jamala won last year's event with the song 1944.
In an open letter published by Strana, the team said: "Hereby we, the Eurovision team, for whom this contest has become not only part of our work but also part of our life, officially inform that we are resigning and stopping work on preparations for the organisation of the contest."
"""

tokenized_data=get(text.lower())

vect=CountVectorizer()

vect.fit(tokenized_data)
#print vect.get_feature_names()
simple_train_dtm=vect.transform(tokenized_data)
#print simple_train_dtm.to_array
#datas=pd.DataFrame(simple_train_dtm.toarray(),columns=vect.get_feature_names)
datas=pd.DataFrame(simple_train_dtm.toarray(),columns=vect.get_feature_names())
'''cols=["word","count"]
words=[]
counts=[]
word_count={
'words' : words,
'counts': counts
}'''


for i in tokenized_data:
    try:
        r_server.rpush(i,datas[i].sum())
    except Exception as e:
        pass
r_server.save
#print word_count
