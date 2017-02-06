from flask import Flask,render_template,request
import pickle
import json
from pprint import pprint
import pickle

app=Flask(__name__)


@app.route("/")
def index():
        x,y=datas()
        return render_template("show.html",data1=x,data2=y)

def datas():

    with open('datas.json') as data_file:
        data = json.load(data_file)

    pprint(data[0]["occurs"])
    data_serialized_file=open("data.pickle","wb")

    pickle.dump(data,data_serialized_file)
    data_serialized_file.close()

    x=pickle.load(open("data.pickle","rb"))

    return x[0]["occurs"],x[0]["word"]



if __name__=="__main__":
    app.run(port=4000)
