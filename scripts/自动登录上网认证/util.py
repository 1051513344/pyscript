import requests
import io
import sys
import urllib3
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def isWifiLogin():
    urllib3.disable_warnings()
    try:
        request = requests.get("https://www.baidu.com", verify=False)
        resp = request.content.decode("utf-8")
        request.close()
        if "<title>百度一下，你就知道</title>" in resp:
            return True
        return False
    except Exception as e:
        return False

