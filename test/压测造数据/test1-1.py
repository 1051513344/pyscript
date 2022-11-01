
# 教学活动计划、科室活动统计、学生活动统计、教师活动统计页面数据加载
import random

import radar
import requests
import json
import datetime
from threading import Thread
from session import getSessionId

with open("domain", 'r') as f:
    domain = f.read()

# 用户管辖科室
def getusermanagerdept():
    url = domain + "/actionplanbase/getusermanagerdept"

    data = {"1":'{"command":"actionplanbase/getusermanagerdept","sessionid":"[sessionid]","loginid":"1","uid":"1","paramcode":"actionplanaddroles"}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    # print(response_json)

    beanlist = response_json["1"]["beanlist"]

    hospitallist = beanlist["hospitallist"]
    baselist = beanlist["baselist"]
    officelist = beanlist["officelist"]
    inpatientarealist = beanlist["inpatientarealist"]
    deptlist = officelist + inpatientarealist

    # print(hospitallist)
    # print(baselist)
    # print(officelist)
    # print(inpatientarealist)
    # print(deptlist)
    return hospitallist, baselist, deptlist

# 主讲人
def getspeaker_Hospital():
    url = domain + "/actionplanbase/getspeaker"

    data = {"1":'{"command":"actionplanbase/getspeaker","sessionid":"[sessionid]","loginid":"1","speakername":"","actionplanlevel":"hospital","deptid":99}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    speakerlist = response_json["1"]["speakerlist"]
    speakerlist = [i['id'] for i in speakerlist]
    print(speakerlist)
    return speakerlist


emptyspeakerlistbase = []
# 主讲人
def getspeaker_Base():
    url = domain + "/actionplanbase/getspeaker"

    hospitallist, baselist, deptlist = getusermanagerdept()

    baseindex = random.randint(-1, len(baselist) - 1)
    baseid = str(baselist[baseindex]['id'])
    if baseid in emptyspeakerlistbase:
        return getspeaker_Base()

    data = {"1":'{"command":"actionplanbase/getspeaker","sessionid":"[sessionid]","loginid":"1","speakername":"","actionplanlevel":"base","deptid":[baseid]}'.replace("[sessionid]", getSessionId()).replace("[baseid]", baseid)}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    speakerlist = response_json["1"]["speakerlist"]
    speakerlist = [i['id'] for i in speakerlist]
    if len(speakerlist) == 0:
        emptyspeakerlistbase.append(baseid)
        return getspeaker_Base()
    return baseid, speakerlist

emptyspeakerlistoffice = []

# 主讲人
def getspeaker_Office(deptlist):
    url = domain + "/actionplanbase/getspeaker"

    if len(deptlist) == 0:
        hospitallist, baselist, deptlist = getusermanagerdept()

    deptindex = random.randint(-1, len(deptlist) - 1)
    deptid = str(deptlist[deptindex]['id'])

    if deptid in emptyspeakerlistoffice:
        return getspeaker_Office(deptlist)

    data = {"1":'{"command":"actionplanbase/getspeaker","sessionid":"[sessionid]","loginid":"1","speakername":"","actionplanlevel":"office","deptid":[deptid]}'.replace("[sessionid]", getSessionId()).replace("[deptid]", deptid)}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    speakerlist = response_json["1"]["speakerlist"]
    speakerlist = [i['id'] for i in speakerlist]

    if len(speakerlist) == 0:
        emptyspeakerlistoffice.append(deptid)
        return getspeaker_Office(deptlist)
    return deptid, speakerlist


# 活动类型
def turnbaseinfolevel():
    url = domain + "/turnbaseinfo/turnbaseinfolevel"

    data = {"1":'{"command":"turnbaseinfo/turnbaseinfolevel","sessionid":"[sessionid]","loginid":"1","code":"teachtype"}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    baseinfolevellist = json.loads(response_json["1"]["baseinfolevellist"])

    return [i['id'] for i in baseinfolevellist]

# 年级

def queryDictionaryList1():
    url = domain + "/traineestudent/queryDictionaryList"

    data = {"1":'{"command":"traineestudent/queryDictionaryList","sessionid":"[sessionid]","loginid":"1","uid":"1","code":"turngrade"}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    return response_json

def randomGrade(dictionaryList):


    gradelist = dictionaryList["1"]["dic_list"]
    gradelist = [i['id'] for i in gradelist]
    # random.randint 左开右闭
    # range 左闭右开
    gradenum = random.randint(0, len(gradelist))
    list = []
    for num in range(0, gradenum):
        gradeindex = random.randint(-1, len(gradelist) - 1)
        if gradelist[gradeindex] not in list:
            list.append(gradelist[gradeindex])

    return list




# 学员类型

def queryDictionaryList2():
    url = domain + "/traineestudent/queryDictionaryList"

    data = {"1":'{"command":"traineestudent/queryDictionaryList","sessionid":"[sessionid]","loginid":"1","uid":"1","code":"stud_type"}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    return response_json

def randomStuType(dictionaryList):


    stutypelist = dictionaryList["1"]["dic_list"]
    stutypelist = [i['id'] for i in stutypelist]
    # random.randint 左开右闭
    # range 左闭右开
    stutypenum = random.randint(0, len(stutypelist))
    list = []
    for num in range(0, stutypenum):
        stutypeindex = random.randint(-1, len(stutypelist) - 1)
        if stutypelist[stutypeindex] not in list:
            list.append(stutypelist[stutypeindex])

    return list



# 基地
def getdeptlist():
    url = domain + "/deptinfo/getdeptlist"

    data = {"1":'{"command":"deptinfo/getdeptlist","sessionid":"[sessionid]","loginid":"1","uid":"1","deptcode":"base"}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    return response_json



def randombaselist(baselist):

    baselist = baselist["1"]["beanlist"]
    baselist = [i['id'] for i in baselist]
    basenum = random.randint(0, len(baselist))
    list = []
    for num in range(0, basenum):
        baseindex = random.randint(-1, len(baselist) - 1)
        if baselist[baseindex] not in list:
            list.append(baselist[baseindex])

    return list


# 正在该基地轮转的学员
def getattender1():
    url = domain + "/actionplanbase/getattender"

    data = {"1":'{"command":"actionplanbase/getattender","sessionid":"[sessionid]","loginid":"1","actionplanlevel":"base","actiontime":"","deptid":100,"baseattend":"turn"}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    return response_json

# 专业在该基地的学员

def getattender2():
    url = domain + "/actionplanbase/getattender"

    data = {"1":'{"command":"actionplanbase/getattender","sessionid":"[sessionid]","loginid":"1","actionplanlevel":"base","actiontime":"","deptid":100,"baseattend":"base"}'.replace("[sessionid]", getSessionId())}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    return response_json


# 学生列表

emptyattenderxingshilist = []

def getattenderforsearch():
    xing_shi = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许",
                "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水", "窦", "章",
                "云", "苏", "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳",
                "酆", "鲍", "史", "唐", "费", "廉", "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "常",
                "乐", "于", "时", "傅", "皮", "卞", "齐", "康", "伍", "余", "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹",
                "姚", "邵", "湛", "汪", "祁", "毛", "禹", "狄", "米", "贝", "明", "臧", "计", "伏", "成", "戴", "谈", "宋", "茅", "庞",
                "熊", "纪", "舒", "屈", "项", "祝", "董", "粱", "杜", "阮", "蓝", "闵", "席", "季", "麻", "强", "贾", "路", "娄", "危",
                "江", "童", "颜", "郭", "梅", "盛", "林", "刁", "钟", "徐", "邱", "骆", "高", "夏", "蔡", "田", "樊", "胡", "凌", "霍",
                "虞", "万", "支", "柯", "昝", "管", "卢", "莫", "经", "房", "裘", "缪", "干", "解", "应", "宗", "丁", "宣", "贲", "邓",
                "郁", "单", "杭", "洪", "包", "诸", "左", "石", "崔", "吉", "钮", "龚", "程", "嵇", "邢", "滑", "裴", "陆", "荣", "翁",
                "荀", "羊", "於", "惠", "甄", "麴", "家", "封", "芮", "羿", "储", "靳", "汲", "邴", "糜", "松", "井", "段", "富", "巫",
                "乌", "焦", "巴", "弓", "牧", "隗", "山", "谷", "车", "侯", "宓", "蓬", "全", "郗", "班", "仰", "秋", "仲", "伊", "宫",
                "宁", "仇", "栾", "暴", "甘", "钭", "厉", "戎", "祖", "武", "符", "刘", "景", "詹", "束", "龙", "叶", "幸", "司", "韶",
                "郜", "黎", "蓟", "薄", "印", "宿", "白", "怀", "蒲", "邰", "从", "鄂", "索", "咸", "籍", "赖", "卓", "蔺", "屠", "蒙",
                "池", "乔", "阴", "欎", "胥", "能", "苍", "双", "闻", "莘", "党", "翟", "谭", "贡", "劳", "逄", "姬", "申", "扶", "堵",
                "冉", "宰", "郦", "雍", "舄", "璩", "桑", "桂", "濮", "牛", "寿", "通", "边", "扈", "燕", "冀", "郏", "浦", "尚", "农",
                "温", "别", "庄", "晏", "柴", "瞿", "阎", "充", "慕", "连", "茹", "习", "宦", "艾", "鱼", "容", "向", "古", "易", "慎",
                "戈", "廖", "庾", "终", "暨", "居", "衡", "步", "都", "耿", "满", "弘", "匡", "国", "文", "寇", "广", "禄", "阙", "东",
                "殴", "殳", "沃", "利", "蔚", "越", "夔", "隆", "师", "巩", "厍", "聂", "晁", "勾", "敖", "融", "冷", "訾", "辛", "阚",
                "那", "简", "饶", "空", "曾", "毋", "沙", "乜", "养", "鞠", "须", "丰", "巢", "关", "蒯", "相", "查", "後", "荆", "红",
                "游", "竺", "权", "逯", "盖", "益", "桓", "公", "万俟", "司马", "上官", "欧阳", "夏侯", "诸葛", "闻人", "东方", "赫连",
                "皇甫", "尉迟", "公羊", "澹台", "公冶", "宗政", "濮阳", "淳于", "单于", "太叔", "申屠", "公孙", "仲孙", "轩辕", "令狐",
                "钟离", "宇文", "长孙", "慕容", "鲜于", "闾丘", "司徒", "司空", "亓官", "司寇", "仉", "督", "子车", "颛孙", "端木",
                "巫马", "公西", "漆雕", "乐正", "壤驷", "公良", "拓跋", "夹谷", "宰父", "谷梁", "晋", "楚", "闫", "法", "汝", "鄢",
                "涂", "钦", "段干", "百里", "东郭", "南门", "呼延", "归", "海", "羊舌", "微生", "岳", "帅", "缑", "亢", "况", "后",
                "有", "琴", "梁丘", "左丘", "东门", "西门", "商", "牟", "佘", "佴", "伯", "赏", "南宫", "墨", "哈", "谯", "笪", "年",
                "爱", "阳", "佟", "第五", "言", "福", "百", "家", "姓", "终", "梁"]

    xingshi = random.choice(xing_shi)

    if xingshi in emptyattenderxingshilist:
        return getattenderforsearch()

    url = domain + "/actionplanbase/getattenderforsearch"

    data = {"1":'{"command":"actionplanbase/getattenderforsearch","sessionid":"[sessionid]","loginid":"1","actionplanlevel":"office","attendername":"[xingshi]"}'.replace("[sessionid]", getSessionId()).replace("[xingshi]", xingshi)}

    response = requests.post(url, data=data)

    response_text = response.text

    response_json = json.loads(response_text)

    attendlist = response_json["1"]["attendlist"]

    if len(attendlist) == 0:
        emptyattenderxingshilist.append(xingshi)
        return getattenderforsearch()

    resultlist = []
    result = {}
    for attend in attendlist:
        result["id"] = attend["id"]
        result["value"] = attend["name"] + "-" + attend["username"]
        resultlist.append(result)
    return resultlist



def attendbusinfo_Base(baseid, actiontime):
    url = domain + "/actionplanbase/getattender"

    baseattend = random.choice(("turn", "base"))

    data = {
            "1": {
                "command": "actionplanbase/getattender",
                "sessionid": getSessionId(),
                "loginid": "1",
                "actionplanlevel": "base",
                "actiontime": actiontime,
                "deptid": baseid,
                "baseattend": baseattend
                }
            }

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)
    grouplistcount = response_json["1"]["result"]["grouplist"][0]["count"]

    if baseattend == "turn":
        return "正在该基地轮转的学员-{}".format(grouplistcount)
    if baseattend == "base":
        return "专业在该基地的学员-{}".format(grouplistcount)

    return grouplistcount



# 随机生成时间段内的时间
# print(radar.random_datetime("2022-01-01T00:00:00", "2022-12-31T23:23:59"))  # 指定范围内随机：年月日 时分秒
def actiontime():

    # random_datetime = radar.random_datetime("2022-01-01T00:00:00", "2022-12-31T23:23:59")
    random_datetime = radar.random_datetime("2022-10-19T00:00:00", "2022-12-31T23:23:59")
    random_datetime = str(random_datetime)
    # print(random_datetime)
    date = random_datetime[0:10]
    startTime = random_datetime[11:16]
    startTime_timestamp = datetime.datetime.strptime(date + " " + startTime + ":00", "%Y-%m-%d %H:%M:%S").timestamp()
    endTime = "23:59"
    endTime_timestamp = datetime.datetime.strptime(date + " " + endTime + ":00", "%Y-%m-%d %H:%M:%S").timestamp()
    # print(endTime_timestamp)
    # print(date)
    # print(startTime)
    # print(endTime)
    actiontime = "[{"+"\"date\":\"{}\",\"startTime\":\"{}\",\"endTime\":\"{}\",\"start\":{},\"end\":{}".format(date, startTime, endTime, str(startTime_timestamp).replace(".0", "000"), str(endTime_timestamp).replace(".0", "000")) + "}]"
    # print(actiontime)
    return actiontime

def getattender_Hospital(gradelist, stdtypelist, basebean):
    url = domain + "/actionplanbase/getattender"

    data = {"1":{"command":"actionplanbase/getattender","sessionid":getSessionId(),"loginid":"1","actionplanlevel":"hospital","actiontime":"[{\"date\":\"2022-10-17T16:00:00.000Z\",\"startTime\":\"00:30\",\"endTime\":\"01:45\",\"start\":1666024200000,\"end\":1666028700000}]","gradebean":{"bustype":"grade","gradelist":gradelist},"stdtypebean":{"bustype":"stdtype","stdtypelist":stdtypelist},"basebean":{"bustype":"base","baselist":basebean}}}

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    print(response_json)
    if len(response_json["1"]["result"]["grouplist"]) > 0:
        return response_json["1"]["result"]["grouplist"][0]["count"]
    return 0



# 院级

def addactionplan_Hospital():

    typelist = turnbaseinfolevel()
    speakerlist = getspeaker_Hospital()
    dictionaryList1 = queryDictionaryList1()
    dictionaryList2 = queryDictionaryList2()
    baselist = getdeptlist()

    for i in range(9223, 10001):
    # for i in range(1, 2):

        theme = "[院级]压测用实习生教学活动{}".format(i)

        typeindex = random.randint(-1, len(typelist) - 1)
        type = typelist[typeindex]

        speakerindex = random.randint(-1, len(speakerlist) - 1)
        speaker = speakerlist[speakerindex]

        randomGradeList = randomGrade(dictionaryList1)
        randomStuTypeList = randomStuType(dictionaryList2)
        randombaseList = randombaselist(baselist)

        attendinfocount = getattender_Hospital(randomGradeList, randomStuTypeList, randombaseList)

        attendinfolist = []

        for rGrade in randomGradeList:
            attendinfolist.append(
                {
                    "attendbusid": rGrade,
                    "attendbusinfo": "{}人".format(attendinfocount),
                    "bustype": "grade",
                    "type": 1
                }
            )

        for rStuType in randomStuTypeList:
            attendinfolist.append(
                {
                    "attendbusid": rStuType,
                    "attendbusinfo": "{}人".format(attendinfocount),
                    "bustype": "type",
                    "type": 1
                }
            )
        for randombase in randombaseList:
            attendinfolist.append(
                {
                    "attendbusid": randombase,
                    "attendbusinfo": "{}人".format(attendinfocount),
                    "bustype": "base",
                    "type": 1
                }
            )
        url = domain + "/actionplan/addactionplan"

        data = {
                "1": {
                    "command": "actionplan/addactionplan",
                    "uid": "1",
                    "sessionid": getSessionId(),
                    "loginid": "1",
                    "actionplanlevel": "hospital",
                    "deptid": 99,
                    "theme": theme,
                    "type": type,
                    "actiontime": actiontime(),
                    "speakerlist": [
                        {
                            "uid": speaker
                        }
                    ],
                    "place": "测试活动地点",
                    "attendinfo": {
                        "actionplanlevel": "hospital",
                        "deptid": 99,
                        "starttime": "Invalid date",
                        "endtime": "Invalid date",
                        "gradebean": {
                            "bustype": "grade",
                            "gradelist": randomGradeList
                        },
                        "stdtypebean": {
                            "bustype": "stdtype",
                            "stdtypelist": randomStuTypeList
                        },
                        "basebean": {
                            "bustype": "baselist",
                            "baselist": randombaseList
                        }
                    },
                    "attendinfolist": attendinfolist,
                    "remark": "",
                    "filelist": []
                    }
                }
        # print(data)
        response = requests.post(url, json=data)

        response_text = response.text

        response_json = json.loads(response_text)

        errcode = response_json["1"]["errcode"]
        if errcode == '0':
            print(theme + " 添加成功！")
        else:
            print(theme + " 添加失败！")
        # print(response_json)

    print("添加院级压测教学活动完成")
    return "添加院级压测教学活动完成"

# 基地级

def addactionplan_Base():

    typelist = turnbaseinfolevel()

    for i in range(1, 20001):
    # for i in range(1, 2):

        url = domain + "/actionplan/addactionplan"

        theme = "[基地级]压测用实习生教学活动{}".format(i)

        typeindex = random.randint(-1, len(typelist) - 1)
        type = typelist[typeindex]

        baseid, speakerlist = getspeaker_Base()
        speakerindex = random.randint(-1, len(speakerlist) - 1)
        speaker = speakerlist[speakerindex]

        action_time = actiontime()

        attendbusinfo = attendbusinfo_Base(baseid, action_time)

        data = {
                "1": {
                    "command": "actionplan/addactionplan",
                    "uid": "1",
                    "sessionid": getSessionId(),
                    "loginid": "1",
                    "actionplanlevel": "base",
                    "deptid": baseid,
                    "theme": theme,
                    "type": type,
                    "actiontime": action_time,
                    "speakerlist": [
                        {
                            "uid": speaker
                        }
                    ],
                    "place": "测试活动地点",
                    "attendinfo": {
                        "actionplanlevel": "base",
                        "deptid": baseid,
                        "actiontime": action_time,
                        "baseattend": "turn"
                    },
                    "attendinfolist": [
                        {
                            "attendbusid": baseid,
                            "attendbusinfo": attendbusinfo,
                            "type": 1,
                            "bustype": "turn"
                        }
                    ],
                    "remark": "",
                    "filelist": []
                    }
                }

        response = requests.post(url, json=data)

        response_text = response.text

        response_json = json.loads(response_text)

        errcode = response_json["1"]["errcode"]
        if errcode == '0':
            print(theme + " 添加成功！")
        else:
            print(theme + " 添加失败！")
        # print(response_json)
    print("添加基地级压测教学活动完成")
    return "添加基地级压测教学活动完成"


# 科室级

def addactionplan_Office():

    url = domain + "/actionplan/addactionplan"

    typelist = turnbaseinfolevel()

    for i in range(14530, 20001):
    # for i in range(1, 2):

        theme = "[科室级]压测用实习生教学活动{}".format(i)

        typeindex = random.randint(-1, len(typelist) - 1)
        type = typelist[typeindex]

        deptid, speakerlist = getspeaker_Office([])
        speakerindex = random.randint(-1, len(speakerlist) - 1)
        speaker = speakerlist[speakerindex]

        attenders = getattenderforsearch()

        attendinfolist = []

        for attender in attenders:
            attendinfolist.append(
                {
                    "attendbusid": attender['id'],
                    "attendbusinfo": attender['value'],
                    "type": 2,
                    "bustype": ""
                }
            )

        data = {
                "1": {
                    "command": "actionplan/addactionplan",
                    "uid": "1",
                    "sessionid": getSessionId(),
                    "loginid": "1",
                    "actionplanlevel": "office",
                    "deptid": deptid,
                    "theme": theme,
                    "type": type,
                    "actiontime": actiontime(),
                    "speakerlist": [
                        {
                            "uid": speaker
                        }
                    ],
                    "place": "测试活动地点",
                    "attendinfo": {},
                    "attendinfolist": attendinfolist,
                    "remark": "",
                    "filelist": []
                    }
                }

        response = requests.post(url, json=data)

        response_text = response.text

        response_json = json.loads(response_text)

        errcode = response_json["1"]["errcode"]
        if errcode == '0':
            print(theme + " 添加成功！")
        else:
            print(theme + " 添加失败！")

        # print(response_json)
    print("添加科室级压测教学活动完成")
    return "添加科室级压测教学活动完成"


def addactionplan_Office_Single_Thread(i, typelist):

    url = domain + "/actionplan/addactionplan"

    theme = "[科室级]压测用实习生教学活动{}".format(i)

    typeindex = random.randint(-1, len(typelist) - 1)
    type = typelist[typeindex]

    deptid, speakerlist = getspeaker_Office([])
    speakerindex = random.randint(-1, len(speakerlist) - 1)
    speaker = speakerlist[speakerindex]

    attenders = getattenderforsearch()

    attendinfolist = []

    for attender in attenders:
        attendinfolist.append(
            {
                "attendbusid": attender['id'],
                "attendbusinfo": attender['value'],
                "type": 2,
                "bustype": ""
            }
        )

    data = {
            "1": {
                "command": "actionplan/addactionplan",
                "uid": "1",
                "sessionid": getSessionId(),
                "loginid": "1",
                "actionplanlevel": "office",
                "deptid": deptid,
                "theme": theme,
                "type": type,
                "actiontime": actiontime(),
                "speakerlist": [
                    {
                        "uid": speaker
                    }
                ],
                "place": "测试活动地点",
                "attendinfo": {},
                "attendinfolist": attendinfolist,
                "remark": "",
                "filelist": []
                }
            }

    response = requests.post(url, json=data)

    response_text = response.text

    response_json = json.loads(response_text)

    errcode = response_json["1"]["errcode"]
    if errcode == '0':
        print(theme + " 添加成功！")
    else:
        print(theme + " 添加失败！")


if __name__=='__main__':
    index = 20006

    threads = []

    typelist = turnbaseinfolevel()

    while index <= 20006 + 681:
        try:
            print("==================开始执行[{}-{}]！".format(index, index+9))
            #多线程
            for i in range(10):#利用循环创建5个线程
                t=Thread(target=addactionplan_Office_Single_Thread, args=(index+i,typelist,))
                #启动线程
                threads.append(t)
                print("{}执行中......".format(index + i))
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            index = index + 10
            threads.clear()
            print("执行[{}-{}]完毕！======================".format(index, index+9))
        except Exception as e:
            print("执行[{}-{}]失败".format(index, index+9))
            break
# addactionplan_Hospital()
# addactionplan_Base()
# addactionplan_Office()