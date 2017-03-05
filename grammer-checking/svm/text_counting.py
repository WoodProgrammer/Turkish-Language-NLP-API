from collections import Counter
import re
#text=open("mobby.txt","r+")
cnt=Counter()
words = re.findall('\w+', open('mobby.txt').read().lower())
#print Counter(words).most_common(10)

for line in words:
	cnt[line]+=1
print cnt['sir']
