from flask import Flask
from redis import Redis
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
redis.rpush("hallo",34)
redis.save
@app.route('/')
def hello_world():
    return 'hallo value is {}'.format(redis.lindex('hallo',0))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
