# -*- coding: gbk -*-
import time
import threading
import schedule
import redis
import os

def check_redis_status():
    #创建Redis客户端
    r = redis.Redis(host='localhost', port=6379)
    response = r.ping()
    if response:
        print("连接成功！")
    else:
        print("连接失败！重启服务")
        os.system("/root/shell/restart-redis.sh")

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(180).seconds.do(run_threaded, check_redis_status)

while True:
    schedule.run_pending()
    time.sleep(1)
