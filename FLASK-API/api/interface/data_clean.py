#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from sklearn.feature_extraction.text import CountVectorizer

import json
from nltk import ngrams, re, pprint
from ngram import NGram
import pandas as pd
import redis
r_server=redis.Redis("localhost")

def get(paragraph):

    tokenized_data = nltk.word_tokenize(paragraph)
    return tokenized_data

str_read='''
Porto'nun tecrubeli kalecisi Iker Casillas'in Sporting macinin son dakikasinda yaptigi inanilmaz kurtaris
geceye damgasini vurdu.Porto'nun Sporting Lizbon'i 2-1 yendigi Portekiz Ligi mucadelesinde Iker Casillas'in yaptigi kurtaris geceye damga vurdu.
Son dakikasina 2-1 girilen karsilasmada Sporting Lizbon'un tum haklariyla yuklendigi bir pozisyonda yapilan kafa vurusunu muthis bir refleksle cikartan Casillas,
 taraftarinin adeta gol sevinci yasamasina sebep oldu. Sporting Lizbon this is
eurovison
'''
text = """The Eurovision Song Contest has hit a major road bump, after 21 top level staff organising the event resigned.
The Ukrainian Eurovision team say they were stripped of major responsibilities in December, when a new boss was appointed to the organising committee.
According to their resignation letter, they were "completely blocked" from making decisions about the show.
The EBU, which founded Eurovision, told Ukraine's public broadcaster to "stick to the timeline" despite the upheaval.
It insisted the event would go ahead as planned in Kiev this May. Among the team members who resigned were two executive producers of this year's show.
All the staff were appointed by the Ukraine Public Broadcaster (UA:PBC), which is organising the contest after Ukrainian singer Jamala won last year's event with the song 1944.
In an open letter published by Strana, the team said: "Hereby we, the Eurovision team, for whom this contest has become not only part of our work but also part of our life, officially inform that we are resigning and stopping work on preparations for the organisation of the contest."
this this this this
"""
def redis_writer(t_name):
    tokenized_data2=get(t_name.lower())
    vect2=CountVectorizer()
    vect2.fit(tokenized_data2)
    #print vect.get_feature_names()
    simple_train_dtm2=vect2.transform(tokenized_data2)
    #print simple_train_dtm.to_array
    #datas=pd.DataFrame(simple_train_dtm.toarray(),columns=vect.get_feature_names)
    datas2=pd.DataFrame(simple_train_dtm2.toarray(),columns=vect2.get_feature_names())
    for i in tokenized_data2:
        try:
            r_server.rpush(i,datas2[i].sum())
        except Exception as e:
            pass
    r_server.save
redis_writer(text)


#print word_count
