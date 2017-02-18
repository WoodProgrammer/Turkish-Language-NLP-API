import redis
from flask import Flask
import json
import unittest
app=Flask(__name__)
r_server=redis.Redis("localhost")
'''r_server.rpush("player_name","Atiba Huthicson")
r_server.rpush("player_name","DEMBABA")
r_server.rpush("player_name","OGUZHAN OZYAKUP")
r_server.rpush("player_name","CENK TOSUN ")
'''
'''for i in range(4):
    x = r_server.lindex("player_name",i)
    data.append(x)'''
@app.route("/")
def index():

    return  json.dumps(r_server.lrange("player_name",0,4))

if __name__=="__main__":
    app.run(debug=True)
    unittest.main()
