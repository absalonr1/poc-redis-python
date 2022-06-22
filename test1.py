from platform import system
import redis
import requests
import os


redisPort = 6379
redisHost = "redis-dev-cluster.kglkzz.ng.0001.usw2.cache.amazonaws.com"

headers = {
    'bx-usercode': os.environ["bx_usercode"],
    'bx-token' : os.environ["bx_token"],
    'bx-client_account': os.environ["bx_client_account"], 
    'content-type': 'application/json' 
}

response = requests.get('https://bx-tracking.bluex.cl/bx-geo/states',headers=headers) #https://jsonplaceholder.typicode.com/users/1
print(response.status_code )
if(response.status_code == 200):
    jsonResp = response.json()
    pais = jsonResp['data']
    for p in pais:
        print("pais name:"+p["name"])
        states = p["states"]
        for s in states:
            print("\t Region: "+s["name"])
            ciudades = s["ciudades"]
            for c in ciudades:
                print("\t\t Ciudad:"+c["name"])
                districts = c["districts"]
                for d in districts:
                    print("\t\t\t district (localidad):"+d["name"]+" | code:"+d["code"])


'''
Original

{ "estadoName": estadoName, "estadoCode": estadoCode, "cidadeName": cidadeName, "cidadeCode": cidadeCode, 
"distritosName": distritosName, "distritosCode": distritosCode, "defaultDistrict": defaultDistrict });

# 1era opcion - Busca por district name & ciudad name == neighborhood
# 2da opcion - Busca solo por ciudad name
# 3da opcion - Busca solo por district name

Nuevas estructuras en Redis
district (name)
		code-district
		defaultDistrict-ciudad
		code-ciudad
		name-ciudad
		code-state(region)
		name-state(region)

ciudad (name)
		code-district
		defaultDistrict-ciudad
		code-ciudad
		name-ciudad
		code-state(region)
		name-state(region)
'''

# r = redis.Redis(host=redisHost, port=redisPort, db=0)
# r.hset("cache:0", "hkey", "hval")
# print(r.hget("cache:0", "hkey"))
# r.hgetall("a")
# r.set('foo', 'bar')
# print(r.get('foo'))
