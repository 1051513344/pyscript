

import requests
import json
import re
import csv

def getToken():

    data = json.dumps({"username":"18888888885","phone":"","pwd":"c4318372f98f4c46ed3a32c16ee4d7a76c832886d887631c0294b3314f34edf1","unionid":0,"ip":"","devicetoken":"","devicetype":0})
    url = 'http://userplat.zwjk.com/api/DjUser/UserLogin'
    headers = {'content-type': 'application/json',
               "appid": "yhzxqd7e0187afeb16e57e4b47e3a92ef8d061"
               }

    resp = requests.post(
        url=url,
        data=data,headers=headers).json()
    token = resp['ret_data']['Token']
    return str(token)


data = {
    'caseTypeName': '["常规","细胞","冰冻"]',
    'type': 0,
    'consultStatusList': "[5, 6]",
    'updateStartTime': "2020-06-01",
    'updateEndTime': "2020-06-30",
    'pageNum': 1,
    'pageSize': 47*10,
    'isCancel': "0"
}




text = requests.post("http://ask.yilian120.com/blinquiry/adminGetConsultList.htm",
                     data=data,
                     headers={"Cookie":"UM_distinctid=1719ffb2fb3771-006b287cdb3d36-b79193d-1fa400-1719ffb2fb41b; DTL_SESSION_ID=2708b4ba-557b-480a-b907-8e957bfffbe0"}
                     ).text
dataJson = json.loads(text)
dataList = dataJson["ret_data"]["list"]
# print(len(dataList))



# 初始化列表
data = []
data.append(("会诊编号", "病理类型", "患者姓名", "部位", "申请医生", "申请医院", "会诊专家", "提交时间", "最后修改时间", "会诊状态"))

dataList = list(dataList)
with open('test.csv', 'a', newline='') as f:
    for i in dataList:
        consultNo = re.findall(r"'consultNo': '(BL.*?)'", str(i))[0]
        caseTypeName = re.findall(r"'caseTypeName': '(.*?)'", str(i))[0]
        name = re.findall(r"'name': '(.*?)'", str(i))[0]
        parts = re.findall(r"'parts': '(.*?)'", str(i))[0]
        doctorName = re.findall(r"'doctorType': 0, 'doctorName': '(.*?)'", str(i))[0]
        hospitalName = re.findall(r"'hospitalName': '(.*?)'", str(i))[0]
        doctorName2 = re.findall(r"'doctorType': 1, 'doctorName': '(.*?)'", str(i))[0]
        commitTime = re.findall(r"'commitTime': '(.*?)'", str(i))[0]
        updateTime = re.findall(r"'updateTime': '(.*?)'", str(i))[0]
        # consultStatus = re.findall(r"'consultStatus': (\d+)", str(i))
        data.append((consultNo, caseTypeName, name, parts, doctorName, hospitalName, doctorName2, commitTime, updateTime, "已诊断"))
    # 实例化csv写数据对象
    writer = csv.writer(f)
    writer.writerows(data)







