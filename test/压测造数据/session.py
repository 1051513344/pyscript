import requests
import json

with open("domain", 'r') as f:
    domain = f.read()

def getSessionId():
    with open("sessionid", 'r') as f:
        sessionid = f.read()
    if sessionidisvalid(sessionid) == False:
        url = domain + "/usr/login"

        data = {"1":{"command":"usr/login","accountname":"admin","password":"b477c144152e8a7bb2648071163bdebf","validpasswordrule":"1","type":100}}

        response = requests.post(url, json=data)

        response_text = response.text

        response_json = json.loads(response_text)

        with open("sessionid", "w") as f:
            f.write(response_json['1']['sessionid'])

        print("新建sessionid {}".format(response_json['1']['sessionid']))
        return response_json['1']['sessionid']
    else:
        # print("使用已有sessionid {}".format(sessionid))
        return sessionid

def sessionidisvalid(sessionid):
    try:
        url = domain + ":8089"

        data = {"1":{"command":"usr/sessionidisvalid","uid":"1","sessionid":sessionid}}

        response = requests.post(url, json=data)

        response_text = response.text

        response_json = json.loads(response_text)
        # print(response_json)
        return response_json["1"]["errvoice"] == '成功'
    except Exception:
        return False


