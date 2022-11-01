
# 考核状态查询的全部页面数据加载
import random

import radar
import requests
import json
import datetime
from session import getSessionId

with open("domain", 'r') as f:
    domain = f.read()

# 轮转科室
def queryTurnDeptList():
    url = domain + "/turn/queryTurnDeptList"

    data = {"1":{"command":"turn/queryTurnDeptList","sessionid":getSessionId(),"loginid":"1","dept_id":99,"type":1}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    dept_id_name_list = []
    dept_list = response_json["1"]["dept_list"]

    for dept in dept_list:
        dept_id_name_list.append(
            {
                'id': str(dept['id']),
                'name': dept['name'],
            }
        )

    return dept_id_name_list


# 实习生列表
def querystdnotintraineeplan(code):
    url = domain + "/traineeplan/querystdnotintraineeplan"

    data = {"1":{"command":"traineeplan/querystdnotintraineeplan","sessionid":getSessionId(),"loginid":"1","code":code}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    traineestudentlist = response_json["1"]["traineestudentlist"]
    traineestudentlist = [i['id'] for i in traineestudentlist]
    print(traineestudentlist)
    return traineestudentlist

# 专业

def queryDictionaryList1():
    url = domain + "/traineestudent/queryDictionaryList"

    data = {"1":{"command":"traineestudent/queryDictionaryList","sessionid":getSessionId(),"loginid":"1","code":"major"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    return response_json

# 年级

def queryDictionaryList2():
    url = domain + "/traineestudent/queryDictionaryList"

    data = {"1":{"command":"traineestudent/queryDictionaryList","sessionid":getSessionId(),"loginid":"1","code":"grade"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    return response_json

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

# 添加本科生
def addstudbatch():

    std_type_dict = {"1": {"name": "留学生", "code": "YCLXS"}, "2": {"name": "本科生", "code": "YCBKS"}, "3": {"name": "外院", "code": "YCWY"}}
    std_type = "3"
    std_name = std_type_dict[std_type]["name"]
    std_code = std_type_dict[std_type]["code"]

    dictionaryList1 = queryDictionaryList1()
    dictionaryList2 = queryDictionaryList2()

    for i in range(46085 + 2, 50001):
        major = random.choice(dictionaryList1['1']['dic_list'])
        grade = random.choice(dictionaryList2['1']['dic_list'])

        name = "压测{}".format(std_name) + "{}".format(i).zfill(5)
        code = "{}".format(std_code) + "{}".format(i).zfill(5)
        mobile = create_phone()
        print("============ 生成手机号 {}".format(mobile))
        data = {
                "1": {
                    "command": "traineestudent/add",
                    "sessionid": getSessionId(),
                    "loginid": "1",
                    "traineestudentlist": [
                        {
                            "name": name,
                            "code": code,
                            "mobile": mobile,
                            "major": major['key'],
                            "grade": grade['key'],
                            "lengthschooling": "1",
                            "sex": random.choice(("0", "1")),
                            "stdtype": std_type,
                            "nationality": "CN",
                            "nation": 442,
                            "cardtype": 71,
                            "cardnum": "123456789",
                            "birthday": datetime.datetime.now().strftime('%Y-%m-%d'),
                            "hospitalid": 99
                        }
                    ]
                    }
                }

        while addstud(data, name) == False:
            mobile = create_phone()
            print("<<<<<<<< 重新生成手机号 {} >>>>>>>>".format(mobile))
            data["1"]["traineestudentlist"][0]["mobile"] = mobile

        print("添加实习生 {}".format(name) + " 成功！")


def addstud(data, name):

    url = domain + "/traineestudent/add"

    response = requests.post(url, json=data)

    response_text = response.text
    print(response_text)
    response_json = json.loads(response_text)

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        return True
    else:
        print("添加实习生 {}".format(name) + " 失败！")
        print(response_json)
        return False

# 添加带教老师
def addtechbatch():
    turnDeptList = queryTurnDeptList()

    depts = []

    for turnDept in turnDeptList:
        depts.append(
            {
                "id": turnDept['id'],
                "name": turnDept["name"],
                "position_id": 569,
                "deleteflag": 0,
                "roles": [
                    {
                        "id": 48
                    }
                ]
            }
        )

    for i in range(1, 50001):
        name = "压测实习生带教" + "{}".format(i).zfill(5)
        username = "YCSXSDJ" + "{}".format(i).zfill(5)
        mobile = create_phone()

        data = {
            "1": {
                "command": "dept/addtech",
                "sessionid": getSessionId(),
                "loginid": "1",
                "name": name,
                "sex": random.choice((0, 1)),
                "username": username,
                "isjointrain": random.choice((0, 1)),
                "mobile": mobile,
                "depts": depts,
                "educational": random.choice(("1", "2", "3", "4")),
                "degree": random.choice(("1", "2", "3")),
                "card_type": 71,
                "card_num": "123456789",
                "technique_id": 559,
                "technique_validate_date": "2022-10-20",
                "technique_engage_date": "2022-10-20",
                "teching_id": 562,
                "teching_validate_date": "2022-10-20",
                "teching_engage_date": "2022-10-20",
                "remark": "压测用",
                "roles": [],
                "doctor_qualification_number": username,
                "birthday": "1992-10"
            }
        }

        while addtech(data, name) == False:
            mobile = create_phone()
            print("<<<<<<<< 重新生成手机号 {} >>>>>>>>".format(mobile))
            data["1"]["traineestudentlist"][0]["mobile"] = mobile
            if addtech(data, name):
                break

        print("添加带教 {}".format(name) + " 成功！")


def addtech(data, name):
    url = domain + "/dept/addtech"

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        return True
    else:
        print("添加带教 {}".format(name) + " 失败！")
        print(response_json)
        return False

def dateinterval(startdatetime, datetuplelist, i):

    delta = datetime.timedelta(days=1)
    startdate = startdatetime.strftime('%Y-%m-%d')
    n_days = startdatetime + delta
    enddate = n_days.strftime('%Y-%m-%d')
    # print((startdate, enddate))
    datetuplelist.append((startdate, enddate))
    j = i + 1
    if i != 263:
        return dateinterval(n_days + delta, datetuplelist, j)
    else:
        return datetuplelist


# 带教老师列表
def gettraineeteacher(id, code):
    url = domain + "/trainee/gettraineeteacher"

    data = {"1":{"command":"trainee/gettraineeteacher","sessionid":getSessionId(),"loginid":"1","page":1,"pagesize":10,"id":id,"tecname": code}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    traineeteacherlist = response_json["1"]["list"]
    traineeteacherlist = [i['tecid'] for i in traineeteacherlist]
    print(traineeteacherlist)
    return traineeteacherlist

# 待入科列表
def traineedetaillistallwait(stdinfo):
    url = domain + "/trainee/traineedetaillistall"

    data = {"1":{"command":"trainee/traineedetaillistall","sessionid":getSessionId(),"loginid":"1","uid":"1","levelcode":"position","levelkey":"9","iscontroldept":"1","pagesize":1,"page":1,"tecname":"","grade":"","deptid":"","yearmonth":"","turnstatus":0,"starttime":"2022-10-01","endtime":"2022-10-31","stdinfo":stdinfo}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    traineedetailidlistall = response_json["1"]["list"]
    # print(traineedetailidlistall)
    return traineedetailidlistall

# 添加实习生轮转
def addtraineeplandetail(code, turndept, datetuple):
    url = domain + "/traineeplan/addtraineeplandetail"
    stuidlist = querystdnotintraineeplan(code)
    traineedetaillist = [{
            "deptid": turndept['id'],
            "deptname": turndept['name'],
            "planbegintime": datetuple[0],
            "planendtime": datetuple[1]
        }]
    # print(traineedetaillist)
    for stuid in stuidlist:

        data = {
                "1": {
                    "command": "traineeplan/addtraineeplandetail",
                    "sessionid": getSessionId(),
                    "loginid": "1",
                    "planid": 45,
                    "stdid": stuid,
                    "traineedetaillist": traineedetaillist
                }
            }

        response = requests.post(url, json=data)

        response_text = response.text

        response_json = json.loads(response_text)

        errcode = response_json["1"]["errcode"]
        if errcode == '0':
            print("学生{} 实习生轮转添加成功！".format(code))
        else:
            print("学生{} 实习生轮转添加失败！".format(code))

# 分配带教老师
def disteacher(id):

    tecid = random.choice(gettraineeteacher(id))

    url = domain + "/trainee/disteacher"

    data = {"1":{"command":"trainee/disteacher","sessionid":getSessionId(),"loginid":"1","id":id,"tecid":tecid}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        print("轮转{} 分配带教{}".format(id, tecid) + " 成功！")
    else:
        print("轮转{} 分配带教{}".format(id, tecid) + " 失败！")

# 分配带教老师
def disteacher_tec(id, tecid):

    url = domain + "/trainee/disteacher"

    data = {"1":{"command":"trainee/disteacher","sessionid":getSessionId(),"loginid":"1","id":id,"tecid":tecid}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        print("轮转{} 分配带教{}".format(id, tecid) + " 成功！")
    else:
        print("轮转{} 分配带教{}".format(id, tecid) + " 失败！")


# 入科

def indept(id):
    url = domain + "/trainee/changeturnstatus"

    data = {"1":{"command":"trainee/changeturnstatus","sessionid":getSessionId(),"loginid":"1","id":id,"turnstatus":"5"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        print("轮转{}".format(id) + " 入科成功！")
    else:
        print("轮转{}".format(id) + " 入科失败！")
    return errcode

# 出科

def outdept(id):
    url = domain + "/trainee/changeturnstatus"

    data = {"1":{"command":"trainee/changeturnstatus","sessionid":getSessionId(),"loginid":"1","id":id,"turnstatus":"10"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        print("轮转{}".format(id) + " 出科成功！")
    else:
        print("轮转{}".format(id) + " 出科失败！")

# 轮转中列表
def traineedetaillistall(stdinfo):
    url = domain + "/trainee/traineedetaillistall"

    data = {"1":{"command":"trainee/traineedetaillistall","sessionid":getSessionId(),"loginid":"1","uid":"1","levelcode":"position","levelkey":"9","iscontroldept":"1","pagesize":1,"page":1,"query_type":"run","stdinfo":stdinfo,"turnstatus":5}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    traineedetailidlistall = response_json["1"]["list"]
    print(traineedetailidlistall)
    return traineedetailidlistall

def add():

    turndeptlist = queryTurnDeptList()
    datetuplelist = dateinterval(datetime.datetime.now(), [], 1)

    for i in range(1, 50001):
        code = "YCBKS" + "{}".format(i).zfill(5)
        for turndept, datetuple in zip(turndeptlist, datetuplelist):
            addtraineeplandetail(code, turndept, datetuple)
            traineedetaillistallwails = traineedetaillistallwait(code)
            if len(traineedetaillistallwails) > 0:
                traineedetail = traineedetaillistallwails[0]
                id = traineedetail["id"]
                # 先入科
                try:
                    indept(id)
                    # 再分配带教
                    username = "YCSXSDJ" + "{}".format(i).zfill(5)
                    tecid = gettraineeteacher(id, username)[0]
                    disteacher_tec(id, tecid)
                except Exception:
                    # 查询轮转中
                    traineedetaillist = traineedetaillistall(traineedetail["stdno"])
                    traineeDetail = traineedetaillist[0]
                    id = traineeDetail["id"]
                    disteacher(id)
                    outdept(id)

if __name__ == "__main__":

    addstudbatch()

