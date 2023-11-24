# -*- coding: gbk -*-
import time
import threading
import schedule
import redis
import os

def check_redis_status():
    #����Redis�ͻ���
    r = redis.Redis(host='localhost', port=6379)
    response = r.ping()
    if response:
        print("���ӳɹ���")
    else:
        print("����ʧ�ܣ���������")
        os.system("/root/shell/restart-redis.sh")

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(180).seconds.do(run_threaded, check_redis_status)

while True:
    schedule.run_pending()
    time.sleep(1)
