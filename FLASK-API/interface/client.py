from flask import Flask,render_template,request
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
        return str(args)

    return render_template("enter_data.html")

if __name__=="__main__":
    app.run(debug=True)
