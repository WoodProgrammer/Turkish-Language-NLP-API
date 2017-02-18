import redis

r_server=redis.Redis("localhost")

'''r_server.rpush("player_name","Atiba Huthicson")
r_server.rpush("player_name","DEMBABA")
r_server.rpush("player_name","OGUZHAN OZYAKUP")
r_server.rpush("player_name","CENK TOSUN ")
'''
'''for i in range(4):
    x = r_server.lindex("player_name",i)
    data.append(x)'''

class DatabaseModules():
    for i in range(4):
        x = r_server.lindex("player_name",i)
        data.append(x)

    def (self):
