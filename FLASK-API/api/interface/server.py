#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import nltk
from flask import Flask,make_response,render_template,request
from flask_restful import Api,reqparse,abort,Resource,fields, marshal
import json
from nltk import ngrams, re, pprint
from ngram import NGram

import redis
r_server=redis.Redis("localhost")
app = Flask(__name__)
api = Api(app)

str_read='''
Porto'nun tecrubeli kalecisi Iker Casillas'in Sporting macinin son dakikasinda yaptigi inanilmaz kurtaris
geceye damgasini vurdu.Porto'nun Sporting Lizbon'i 2-1 yendigi Portekiz Ligi mucadelesinde Iker Casillas'in yaptigi kurtaris geceye damga vurdu.
Son dakikasina 2-1 girilen karsilasmada Sporting Lizbon'un tum haklariyla yuklendigi bir pozisyonda yapilan kafa vurusunu muthis bir refleksle cikartan Casillas,
 taraftarinin adeta gol sevinci yasamasina sebep oldu. Sporting Lizbon this is

'''
def abort_if_nothing(person_id):
    if person_id not in datas:
        abort(404, status="{}".format(person_id)+"not here!")

'''@api.representation('application/xml')
def xml(data, code, headers):
    resp = make_response(convert_data_to_xml(datas), code)
    resp.headers.extend(headers)
    return resp'''

class Text(Resource):

    def get(self,person_id):
        n=2
        occurs=[]
        grams_arr=[]
        sixgrams = ngrams(str_read.split(), n)
        for grams in sixgrams:
            #print str(grams)
            x=NGram.compare('{}'.format(person_id.decode('latin-1')),str(grams))
            occurs.append(x)
            grams_arr.append(str(grams))

        main_fields={'occurs':fields.String,"word":fields.String,"freq":fields.String}
        datas={'occurs':"{}".format(max(occurs)*1000),'word':"{}".format(grams_arr[occurs.index(max(occurs))]),'freq':r_server.lindex(person_id,0)}
        x=marshal(datas,main_fields)
        #json.dumps(marshal(datas,main_fields))
        return x
    @app.route("/api")
    def api():

        return render_template('results.html',response_data="asd")



class Tokenize(Resource):
    def get(self,paragraph):
        freq=[]
        words=[]
        tokenized_data = nltk.word_tokenize(paragraph)
        for i in tokenized_data:
            try:
                freq_db=r_server.lindex(i,0)
                words.append(i)
                freq.append(freq_db)

            except Exception as e:
                pass
        main_fields={"word":fields.String,"freq":fields.String}
        datas={'word':words,'freq':freq}
        x=marshal(datas,main_fields)

        return x

api.add_resource(Text, '/api/<person_id>')
api.add_resource(Tokenize, '/tokenize/<paragraph>')

if __name__=="__main__":

    try:
        app.run(debug=True,threaded=True,port=int(sys.argv[1]))
    except Exception as e:
        app.run(debug=True,threaded=True,port=5000)
