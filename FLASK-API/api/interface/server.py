#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import nltk
from flask import Flask,make_response,render_template,request,jsonify
from flask_restful import Api,reqparse,abort,Resource,fields, marshal
import json
from nltk import ngrams, re, pprint
from ngram import NGram

import redis
r_server=redis.Redis("localhost")
app = Flask(__name__)
api = Api(app)


def abort_if_nothing(param_word):
    if param_word not in datas:
        abort(404, status="{}".format(param_word)+"not here!")

'''@api.representation('application/xml')
def xml(data, code, headers):
    resp = make_response(convert_data_to_xml(datas), code)
    resp.headers.extend(headers)
    return resp'''

class Text(Resource):

    def get(self,param_word):
        status=False
        n=2
        occurs=[]
        grams_arr=[]
        words=[]
        for key in r_server.scan_iter():
            words.append(key)

        #sixgrams = ngrams(str_read.split(), n)
        for keys in words:
            #print str(grams)
            x=NGram.compare('{}'.format(param_word.decode('latin-1')),str(keys))
            occurs.append(x)
            grams_arr.append(str(keys))

        for key in r_server.scan_iter():
            if key == param_word:
                status=True


        if status is True:
            main_fields_true={"word":fields.String,"status":fields.Boolean}
            datas_true={'word':"{}".format(param_word),'status':status}
            x_true=marshal(datas_true,main_fields_true)
            return x_true
        else:
            main_fields_false={'occurs':fields.String,"word":fields.String,"freq":fields.String,"status":fields.Boolean}
            datas_false={'occurs':"{}".format(max(occurs)*1000),'word':"{}".format(grams_arr[occurs.index(max(occurs))]),'freq':r_server.get(param_word),'status':status}
            x_false=marshal(datas_false,main_fields_false)
            return x_false

        #json.dumps(marshal(datas,main_fields))
        #if datas["status"]==True:
        #    return datas["word"]
        #else:

    @app.route("/api")
    def api():

        return render_template('results.html',response_data="asd")


class Validators(Resource):
    def get(self,paragraph):
        word_true=[]
        paragraph_arr=paragraph.split()
        for i in paragraph_arr:
            for db_word in r_server.scan_iter():
                if i== db_word:
                    word_true.append(i)
                    break
        #accuracy=paragraph[:]-word_true[:]
        main_fields={'true_words':fields.String,"all_words":fields.String,"accuracy":fields.Integer}
        diff=set(paragraph_arr)-set(word_true)
        accuracy=100-len(diff)*10
        datas={'true_words':word_true,"all_words":paragraph,"accuracy":accuracy}
        x=marshal(datas,main_fields)

        return x

api.add_resource(Text, '/api/<param_word>')
api.add_resource(Validators, '/validators/<paragraph>')

if __name__=="__main__":

    try:
        app.run(debug=True,threaded=True,port=int(sys.argv[1]))
    except Exception as e:
        app.run(debug=True,threaded=True,port=6000)
