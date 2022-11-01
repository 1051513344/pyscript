
# 考勤管理全部页面数据加载

from sql.query.queryDataFunc import QueryDB
from sql.insert.insertDataFunc import InsertDB
import random
import radar
import requests
import json
import datetime
from session import getSessionId

with open("domain", 'r') as f:
    domain = f.read()

def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(1, 4)]
    #第三位数字
    third = {3: random.randint(0, 9),
             4: [5, 7, 9][random.randint(0, 2)],
             5: [i for i in range(10) if i != 4][random.randint(0, 8)],
             7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
             8: random.randint(0, 9), }[second]

    # second = [6,9][random.randint(0, 1)]
    # third = {6: random.randint(0, 9),
    #          9: random.randint(0, 9), }[second]
    # 最后八位数字
    suffix = random.randint(9999999, 100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)

def queryDictionaryList1():
    url = domain + "/turnbaseinfo/turnbaseinfolevel"

    data = {"1":{"command":"turnbaseinfo/turnbaseinfolevel","sessionid":getSessionId(),"loginid":"1","code":"turngrade"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    return response_json

def queryBaseList():
    url = domain + "/turn/queryBaseList"

    data = {"1":{"command":"turn/queryBaseList","sessionid":getSessionId(),"loginid":"1"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    return response_json

def querylevellist():
    url = domain + "/hr/querylevellist"

    data = {"1":{"command":"hr/querylevellist","sessionid":getSessionId(),"loginid":"1","code":"stud_type"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    return response_json

def getdictionaryinfolist():
    url = domain + "/dictionaryinfo/getdictionaryinfolist"

    data = {"1":{"command":"dictionaryinfo/getdictionaryinfolist","sessionid":getSessionId(),"loginid":"1","code":"turnyears"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    return response_json

# 添加住培
def addstudbatch():

    dictionaryList1 = queryDictionaryList1()
    baseList = queryBaseList()
    levellist = querylevellist()
    dictionaryinfolist = getdictionaryinfolist()

    for i in [7262, 14855, 17096, 20166, 28729, 29766, 29767, 31081, 34208, 39274, 39649, 42456, 42615, 47047]:

        turngrade = random.choice(json.loads(dictionaryList1['1']['baseinfolevellist']))['id']
        base = random.choice(baseList['1']['base_list'])['id']
        type = random.choice(levellist['1']['levellist'])['id']
        years = random.choice(dictionaryinfolist['1']['beanlist'])['id']

        name = "压测住院医" + "{}".format(i).zfill(5)
        username = "YCZYY" + "{}".format(i).zfill(5)
        mobile = create_phone()
        print("============ 生成手机号 {}".format(mobile))
        data = {
                "1": {
                    "command": "student/add",
                    "sessionid": getSessionId(),
                    "loginid": "1",
                    "studentlist": [
                        {
                            "turngrade": turngrade,
                            "name": name,
                            "sex": random.choice((0, 1)),
                            "mobile": mobile,
                            "username": username,
                            "base": base,
                            "years": years,
                            "type": type,
                            "birthday": ""
                        }
                    ]
                    }
                }

        flag = False
        while flag == False:
            flag = addstud(data, name)
            if flag == False:
                mobile = create_phone()
                print("<<<<<<<< 重新生成手机号 {} >>>>>>>>".format(mobile))
                data["1"]["studentlist"][0]["mobile"] = mobile

        print("添加住院医 {}".format(name) + " 成功！")


def addstud(data, name):

    url = domain + "/student/add"

    response = requests.post(url, json=data)

    response_text = response.text
    print(response_text)
    response_json = json.loads(response_text)
    if "message" in response_json:
        if response_json["message"] == '请稍后重试':
            return True

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        return True
    else:
        print("添加住院医 {}".format(name) + " 失败！")
        print(response_json)
        if response_json["1"]["errdesc"] == 'session invalid':
            data['1']['sessionid'] = getSessionId()
        return False

if __name__ == "__main__":


    # addstudbatch()

    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "password"
    db = "db"
    charset = "charset"
    table_name = "table_name"

    # 获取需要导出的数据
    q = QueryDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )

    压测住院医id_names = q.queryByCustom("select id,name from Users where name like '压测住院医%'")

    i = InsertDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )

    i.execute_custom(6, 压测住院医id_names)




