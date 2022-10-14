import pypinyin
import requests
import json
# 不带声调的(style=pypinyin.NORMAL)
def to_pin_yin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

role_url = "http://192.168.3.191/role/searchrole"
request_body = {"1": '{"command": "role/searchrole", "sessionid": "7414e20b4056606de01dd50814e402e8", "loginid": "1", "filteredinfo": ""}'}

response = requests.post(role_url, data=request_body)

response_data = response.text
response_data_json = json.loads(response_data)
roleList = response_data_json["1"]["roleList"]

for role in roleList:
    print(to_pin_yin(role["name"]) + "\t" + "ZJ2022@xyjpt" + "\t" + role["name"])