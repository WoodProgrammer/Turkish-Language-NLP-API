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
from test import *
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

        word=max_P(param_word)

    #    main_fields_false={'occurs':fields.String,"word":fields.String,"freq":fields.String,"status":fields.Boolean}
    #    datas_false={'occurs':"{}".format(max(occurs)*1000),'word':"{}".format(grams_arr[occurs.index(max(occurs))]),'freq':r_server.get(param_word),'status':status}
    #    x_false=marshal(datas_false,main_fields_false)
        return word


class Validators(Resource):
    def get(self,paragraph):

        return x

api.add_resource(Text, '/api/<param_word>')
api.add_resource(Validators, '/validators/<paragraph>')

if __name__=="__main__":


        app.run(debug=True,threaded=True,port=6000)
