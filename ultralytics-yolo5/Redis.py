import redis
import os
import time
redis_host = "localhost"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
while(1):
    kelas = r.get("kelas")
    conf = r.get("conf")
    #print(kelas)
    #print(conf)
    print(f"{kelas} = {conf}")
    time.sleep(0.5)
s.close
# 192.168.100.79
