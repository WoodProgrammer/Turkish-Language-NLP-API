from spell import *
import sys
from collections import Counter
WORDS = Counter(words(open('eng.txt').read()))

def max_P(x):
    x=correction(x)
    occurs=[]
    words=[]
    for i in x:
        occur=float(WORDS[i])/sum(WORDS.values())
        occurs.append(occur)
        words.append(i)

    word_index = occurs.index(max(occurs))
    return words[word_index]
