from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
'''
simple_train = ['call you tonight', 'Call me a cab', 'please call me... PLEASE!']
vect = CountVectorizer()
vect.fit(simple_train)
vect.get_feature_names()
vectorized_data=pd.DataFrame(simple_train_dtm.toarray(), columns=vect.get_feature_names())
'''
vect = CountVectorizer()
str_read=['''
Porto'nun tecrubeli kalecisi Iker Casillas'in Sporting macinin son dakikasinda yaptigi inanilmaz kurtaris
geceye damgasini vurdu.Porto'nun Sporting Lizbon'i 2-1 yendigi Portekiz Ligi mucadelesinde Iker Casillas'in yaptigi kurtaris geceye damga vurdu.
Son dakikasina 2-1 girilen karsilasmada Sporting Lizbon'un tum haklariyla yuklendigi bir pozisyonda yapilan kafa vurusunu muthis bir refleksle cikartan Casillas,
 taraftarinin adeta gol sevinci yasamasina sebep oldu. Sporting Lizbon this is
''']


vect.fit(str_read)
vect_str_data=vect.transform(str_read)
datas_sum = np.sum(vect_str_data.toarray(), axis=0)

'''data_train=pd.DataFrame(vect_str_data.toarray(),columns=vect.get_feature_names())
x=data_train["sporting"].count'''
print datas_sum
tokens = vect.get_feature_names()
data_train=pd.DataFrame({'tokens':tokens,'count':datas_sum}).sort('count')
print data_train
