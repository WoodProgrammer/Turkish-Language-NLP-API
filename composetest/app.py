from flask import Flask,make_response,render_template,request
from flask_restful import Api,reqparse,abort,Resource,fields, marshal
import json
from nltk import ngrams, re, pprint
from ngram import NGram
from subprocess import call
from redis import Redis
redis=Redis(host="redis",port=6379)
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
            x=NGram.compare('{}'.format(person_id),str(grams))
            occurs.append(x)
            grams_arr.append(str(grams))

        main_fields={'occurs':fields.String,"word":fields.String}
        datas={'occurs':"{}".format(max(occurs)*1000),'word':"{}".format(grams_arr[occurs.index(max(occurs))])}
        x=marshal(datas,main_fields)
        #json.dumps(marshal(datas,main_fields))
        return x



class Redis1(Resource):
    def get(self,id_redis):
        return str(redis.lindex(id_redis,0))


api.add_resource(Text, '/api/<person_id>')
api.add_resource(Redis1,'/redis/<id_redis>')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)

'''from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
redis.rpush("hallo",12)
@app.route('/')
def hello():
    count = redis.lindex('hallo',0)
    return 'Hello World! I have been seen  times.{}\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
'''
