#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')

from sklearn.feature_extraction.text import CountVectorizer



simple_train=["nerdesin ","zaman","hayat","ılık","sut","ne zaman zaman zaman geleceksin","zamani gelince"]


vect=CountVectorizer()

vect.fit(simple_train)
#print vect.get_feature_names()
simple_train_dtm=vect.transform(simple_train)
#print simple_train_dtm.to_array
#datas=pd.DataFrame(simple_train_dtm.toarray(),columns=vect.get_feature_names)
print simple_train_dtm.toarray()
datas=pd.DataFrame(simple_train_dtm.toarray(),columns=vect.get_feature_names())
print datas["zaman"].sum()
