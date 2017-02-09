from flask import Flask,render_template,request
import requests

from flask_restful import reqparse
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
        api_data=requests.get('http://localhost:5000/api/{}'.format(api_word)).content

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
    app.run(port=4000,debug=True)
