import json
from pprint import pprint
import pickle

with open('datas.json') as data_file:
    data = json.load(data_file)

pprint(data[0]["occurs"])
data_serialized_file=open("data.pickle","wb")

pickle.dump(data,data_serialized_file)
data_serialized_file.close()

x=pickle.load(open("data.pickle","rb"))
#print x[0]["occurs"]
print zip(x[0]["occurs"],x[0]["word"])
