#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from sklearn.feature_extraction.text import CountVectorizer
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask,render_template,request,jsonify
import requests
import json
from flask_restful import reqparse

from jinja2 import Template

parser = reqparse.RequestParser()
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def send():

    if request.method=="POST":
        parser = reqparse.RequestParser()
        word=request.form['word']
        parser.add_argument('word', action='append')
        args = parser.parse_args()
        api_word=str(unicode(args['word'][0]))
        api_data=requests.get('http://localhost:5000/api/{}'.format(api_word.lower())).content

                #SEND GET REQUEST TO THE SERVER.

        return render_template("enter_data.html",api_data=api_data)

    return render_template("enter_data.html")

@app.route('/tokenize',methods=["GET","POST"])
def tokenize():
    if request.method=="POST":
        parser = reqparse.RequestParser()
        word=request.form['paragraph']
        parser.add_argument('paragraph', action='append')
        args = parser.parse_args()
        api_word=str(unicode(args['paragraph'][0].lower()))
        api_data=requests.get('http://localhost:5000/tokenize/{}'.format(api_word)).content
                #SEND GET REQUEST TO THE SERVER.
        api_data2=json.loads(api_data)
        word_template=[]

        for i in range(2) :
            word_template.append(api_data2['word'][i])



        return render_template("paragraph_data.html",api_data = word_template)

    return render_template("paragraph.html")


@app.route('/document-validator',methods=["GET","POST"])
def validators():

    if request.method=="POST":
        parser = reqparse.RequestParser()
        word=request.form['word']
        parser.add_argument('word', action='append')
        args = parser.parse_args()
        api_word=str(unicode(args['word'][0]))
        api_data=requests.get('http://localhost:5000/api/{}'.format(api_word.lower())).content

        return render_template("enter_data.html",api_data=api_data)

    return render_template("enter_data.html")


'''
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/some-url')
def get_data():
    return requests.get('localhost:5000/api/thiz').content
'''
if __name__=="__main__":
    app.run(port=4000,debug=True,threaded=True)
