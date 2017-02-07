from flask import Flask,render_template,request,make_response
from flask_restful import Api,reqparse,Api,abort,Resource,fields, marshal
import pickle

@app.route('/send',methods=["GET","POST"])
def send(self):

    if request.method=="POST":
        parser = reqparse.RequestParser()
        word=request.form['word']
        parser.add_argument('word', action='append')
        args = parser.parse_args()
        word_data=str(args['word'][0])
        return word_data
        
    return render_template("enter_data.html")


api.add_resource(Text, '/api/<person_id>')
if __name__=="__main__":
    app.run(port=6000)
