
# 出科考核成绩页面数据加载
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
def querystdnotintraineeplan():
    url = domain + "/traineeplan/querystdnotintraineeplan"

    data = {"1":{"command":"traineeplan/querystdnotintraineeplan","sessionid":getSessionId(),"loginid":"1","code":""}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    traineestudentlist = response_json["1"]["traineestudentlist"]
    traineestudentlist = [i['id'] for i in traineestudentlist]
    print(traineestudentlist)
    return traineestudentlist


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

# datetuplelist = dateinterval(datetime.datetime.now(), [], 1)
# print(datetuplelist)

# 带教老师列表
def gettraineeteacher(id):
    url = domain + "/trainee/gettraineeteacher"

    data = {"1":{"command":"trainee/gettraineeteacher","sessionid":getSessionId(),"loginid":"1","page":1,"pagesize":10,"id":id}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    traineeteacherlist = response_json["1"]["list"]
    traineeteacherlist = [i['tecid'] for i in traineeteacherlist]
    print(traineeteacherlist)
    return traineeteacherlist


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


added_student_id_list = [9, 10]

# 添加实习生轮转
def addtraineeplandetail():
    url = domain + "/traineeplan/addtraineeplandetail"
    stuidlist = querystdnotintraineeplan()
    turndeptlist = queryTurnDeptList()
    datetuplelist = dateinterval(datetime.datetime.now(), [], 1)
    print(len(turndeptlist))
    print(len(datetuplelist))
    traineedetaillist = []
    for turndept,datetuple in zip(turndeptlist,datetuplelist):
        traineedetaillist.append(
            {
                "deptid": turndept['id'],
                "deptname": turndept['name'],
                "planbegintime": datetuple[0],
                "planendtime": datetuple[1]
            }
        )
    # print(traineedetaillist)
    stunum = 0
    for stuid in stuidlist:

        data = {
                "1": {
                    "command": "traineeplan/addtraineeplandetail",
                    "sessionid": getSessionId(),
                    "loginid": "1",
                    "planid": 44,
                    "stdid": stuid,
                    "traineedetaillist": traineedetaillist
                }
            }

        response = requests.post(url, json=data)

        response_text = response.text

        response_json = json.loads(response_text)

        errcode = response_json["1"]["errcode"]
        if errcode == '0':
            print("学生{}".format(stunum) + " 添加成功！")
            added_student_id_list.append(stuid)
            print("已添加学生id", added_student_id_list)
            stunum = stunum + 1
        else:
            print("学生{}".format(stunum) + " 添加失败！")

    print("添加压测实习生轮转完成")
    return "添加压测实习生轮转完成"


# 待入科列表
def traineedetaillistallwait():
    url = domain + "/trainee/traineedetaillistall"

    data = {"1":{"command":"trainee/traineedetaillistall","sessionid":getSessionId(),"loginid":"1","uid":"1","levelcode":"position","levelkey":"9","iscontroldept":"1","pagesize":1,"page":1,"tecname":"","grade":"","deptid":"","yearmonth":"","turnstatus":0,"starttime":"2022-10-01","endtime":"2022-10-31"}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    traineedetailidlistall = response_json["1"]["list"]
    # print(traineedetailidlistall)
    return traineedetailidlistall


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
        print(response_json)
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

# 考官

def queryexaminerlist(dept_id):
    url = domain + "/traineeexam/queryexaminerlist"

    data = {"1":{"command":"traineeexam/queryexaminerlist","sessionid":getSessionId(),"loginid":"1","dept_id":str(dept_id),"search_info":""}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    examinerlist = response_json["1"]["dept_teach_list"]
    examinerlist = [i['tecid'] for i in examinerlist]
    print(examinerlist)
    return examinerlist



# 考试项目

def queryexamitemlist(deptid):
    url = domain + "/turnannualresult/queryexamitemlist"

    data = {"1":{"command":"turnannualresult/queryexamitemlist","sessionid":getSessionId(),"loginid":"1","examitemname":"","status":"","pagenum":"","pagepersize":"","deptid":deptid}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    examitemlist = response_json["1"]["examitemlist"]
    examitemlist = [i['examitemid'] for i in examitemlist]
    # print(examitemlist)
    return examitemlist


# 被考核学员

def detaillistall(deptid, examTypeId, stdinfo):
    url = domain + "/traineeexam/detaillistall"

    data = {"1":{"command":"traineeexam/detaillistall","sessionid":getSessionId(),"loginid":"1","turnstatus":5,"deptid":deptid,"stdinfo":stdinfo,"examType":examTypeId}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    list = response_json["1"]["list"]
    stu = list[0]
    return stu['stdid'], stu['traineescoreid']


def datetimeinterval():
    datetimetuplelist = []
    datetuplelist = dateinterval(datetime.datetime.now(), [], 1)

    for datetuple in datetuplelist:
        datetimetuplelist.append(
            (datetuple[0] + " 00:00:00", datetuple[1] + " 23:59:59")
        )
    return datetimetuplelist

from  threading import Thread
def add():
    url = domain + "/traineeexam/add"

    datetimetuplelist = datetimeinterval()

    for i in range(0, 50000):

        datetimetuple = random.choice(datetimetuplelist)
        startTime,endTime = datetimetuple[0],datetimetuple[1]

        traineedetaillistallwails = traineedetaillistallwait()

        for traineedetail in traineedetaillistallwails:
            id = traineedetail["id"]
            examTypeId = random.choice((4798, 4813))
            deptId = 0
            try:
                # 先入科
                indept(id)
                # 查询轮转中
                traineedetaillist = traineedetaillistall(traineedetail["stdno"])
                traineeDetail = traineedetaillist[0]
                # 再分配带教
                id = traineeDetail["id"]
                disteacher(id)

                deptId = traineeDetail["deptid"]
                tecid = random.choice(queryexaminerlist(deptId))

                stdid, tsid = detaillistall(deptId, examTypeId, traineedetail["stdname"])

                if examTypeId == 4813:
                    data = {"1":{"command":"traineeexam/add","sessionid":getSessionId(),"loginid":"1","deptId":deptId,"startTime":startTime,"endTime":endTime,"examTypeId":examTypeId,"examType":"3","place":"测试考核地点","remark":"","teclist":[tecid],"stdlist":[{"tsid":tsid,"stdid":stdid}],"examitemlist":[]}}
                if examTypeId == 4798:
                    examitem = random.choice(queryexamitemlist(deptId))
                    data = {"1":{"command":"traineeexam/add","sessionid":getSessionId(),"loginid":"1","deptId":deptId,"startTime":startTime,"endTime":endTime,"examTypeId":examTypeId,"examType":"1","place":"测试考核地点","remark":"","teclist":[tecid],"stdlist":[{"tsid":tsid,"stdid":stdid}],"examitemlist":[examitem]}}

                response = requests.post(url, json=data)

                response_text = response.text

                response_json = json.loads(response_text)

                errcode = response_json["1"]["errcode"]
                if errcode == '0':
                    print("轮转{} 姓名 {} 科室 {}".format(id, traineeDetail["stdname"], traineeDetail["deptname"]) + " 添加出科考核成绩成功！")
                    outdept(id)
                else:
                    print("轮转{} 姓名 {} 科室 {}".format(id, traineeDetail["stdname"], traineeDetail["deptname"]) + " 添加出科考核成绩失败！")
                    break
            except Exception as e:
                print("轮转{} 姓名 {} 科室id {} 科室 {}".format(id, traineeDetail["stdname"], deptId, traineeDetail["deptname"]) + " 添加出科考核成绩失败！", e)
                outdept(traineeDetail['id'])
                break
add()