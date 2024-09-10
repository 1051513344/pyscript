# -*- coding: gbk -*-



# import json
#
# with open("test.json", "r", encoding="utf-8") as f:
#     resp = f.read()
# workHours = 0
# annualDeductHoilday = 0
# respJson = json.loads(resp)
# data = respJson['data']
# # d = data[10]
# d = data[9]
# print(d["userName"])
# dateDetailList = d['dateDetailList']
# for dateDetail in dateDetailList:
#     scheduleList = dateDetail['scheduleList']
#     for schedule in scheduleList:
#         if schedule['workHours'] is not None:
#             workHours += schedule['workHours']
#             print(workHours)
#         if schedule['annualHolidayHoursMinusO'] is not None and schedule['deductHoilday'] == "annual" and dateDetail['workDayFlag']:
#             annualDeductHoilday += schedule['annualHolidayHoursMinusO']
#
# print(workHours / 60 - 40)
# print(annualDeductHoilday)
# import json
#
# s = """        int sexHeaderSize = 3;
#         for (int i = 0; i < sexHeaderSize; i++) {
#             addHeader("男女分布",4000);
#         }
#         int titleHeaderSize = 7;
#         for (int i = 0; i < titleHeaderSize; i++) {
#             addHeader("职称分布",4000);
#         }
#         int levelHeaderSize = 7;
#         for (int i = 0; i < levelHeaderSize; i++) {
#             addHeader("层级分布",4000);
#         }
#         int positionHeaderSize = 12;
#         for (int i = 0; i < positionHeaderSize; i++) {
#             addHeader("职务分布",4000);
#         }
#         int ageHeaderSize = 7;
#         for (int i = 0; i < ageHeaderSize; i++) {
#             addHeader("年龄段分布",4000);
#         }
#         int eduHeaderSize = 9;
#         for (int i = 0; i < eduHeaderSize; i++) {
#             addHeader("学历分布",4000);
#         }
#         int postHeaderSize = 3;
#         for (int i = 0; i < postHeaderSize; i++) {
#             addHeader("岗位类别分布",4000);
#         }
#         int natureHeaderSize = 11;
#         for (int i = 0; i < natureHeaderSize; i++) {
#             addHeader("职工性质分布",4000);
#         }
#         int workYearHeaderSize = 7;
#         for (int i = 0; i < workYearHeaderSize; i++) {
#             addHeader("工作年限分布",4000);
#         }
#         int specialtyHeaderSize = 6;
#         for (int i = 0; i < specialtyHeaderSize; i++) {
#             addHeader("专科护士分布",4000);
#         }
#         int hosYearHeaderSize = 7;
#         for (int i = 0; i < hosYearHeaderSize; i++) {
#             addHeader("到院年限",4000);
#         }
#         int tcmHeaderSize = 3;
#         for (int i = 0; i < tcmHeaderSize; i++) {
#             addHeader("中医院校分布",4000);
#         }
#         int professionHeaderSize = 3;
#         for (int i = 0; i < professionHeaderSize; i++) {
#             addHeader("专业类别",4000);
#         }
#         int statusHeaderSize = 2;
#         for (int i = 0; i < statusHeaderSize; i++) {
#             addHeader("在职状态",4000);
#         }"""
# l1 = []
# l2 = []
# for i in s.split("\n"):
#     if i.startswith("            addHeader"):
#         l1.append(i.replace("            addHeader(\"", "").replace("\",4000);", ""))
#     if "Size = " in i:
#         l2.append(int(i.split(" ")[-1].replace(";", "")))
# d = {}
# for x,y in zip(l1, l2):
#     d[x] = y
# print(json.dumps(d, ensure_ascii=False))

# s = "com.bozhong.nurseae.dao,com.bozhong.nursebase.mapper,com.bozhong.transform.mapper,com.bozhong.inhospitalqc.dao,com.bozhong.performance.dao,com.bozhong.plan.dao,com.bozhong.satisfaction.mapper,com.bozhong.schedule.dao,com.bozhong.nursestaff.dao,com.bozhong.nursetrain.mapper,com.bozhong.form.dao,com.bozhong.nursecollection.dao"
# x = ""
# for i in s.split(","):
#     x = x+'"'+i+'", '
# print(x)
# import re
# with open("../scripts/mybatisLogDDL检查字段长度/DDL.sql", "r") as f:
#     ddl = f.read()
# cdict = {}
# for column in ddl.split("\n"):
#     r = re.findall("\((\d+)\)", column)
#     if len(r) > 0:
#         co = column
#         c = ""
#         x = False
#         for char in co:
#             if char == " ":
#                 if x:
#                     break
#                 continue
#             else:
#                 c = c + char
#                 x = True
#         cdict[c] = r[0]
# # print(cdict)
# #
# with open('../scripts/mybatisLogDDL检查字段长度/test.txt', "r", encoding='utf-8') as f:
#     x = f.read()
# with open('../scripts/mybatisLogDDL检查字段长度/text2.txt', "r", encoding='utf-8') as f:
#     y = f.read()
# l = x.split(", ")
# l2 = y.split(", ")
# for i1,i2 in zip(l, l2):
#     print(i1,"\t"+ i2,"\t"+ str(len(i2.replace("(String)", "").replace("(Integer)", "").replace("(Double)", ""))) if i2 is not None and i2 != 'null' else 0, cdict[i1] if i1 in cdict else '0', "--------------------------------------------" if (len(i2.replace("(String)", "").replace("(Integer)", "").replace("(Double)", "")) if i2 is not None and i2 != 'null' else 0) > (int(cdict[i1]) if i1 in cdict else 0) else "")
#
# with open('../scripts/mybatisLogDDL检查字段长度/text3.txt', "r", encoding='utf-8') as f:
#     sqllog = f.read()


# score_result = re.findall(".*, (\[\{\".*?\"\}\])\(String\),", sqllog)
# for score in score_result:
#     print(score, len(score), cdict['SCORE_CONTENT'])


# x = "xxxx"
# print(f"{{{x}}}")
# print(round(1))

# x = [1, 2, 3, 4]
# for i in x:
#     if x.index(i) > 2:
#         print("xx", i)

# import json
#
# with open("test.json", "r", encoding="utf-8") as f:
#     resp = f.read()
# respJson = json.loads(resp)
# data = respJson['data']
# num = 0
# propertyNameList = []
# for d in data:
#     dossierConfigList = d['dossierConfigList']
#     for dossierConfig in dossierConfigList:
#         propertyName = dossierConfig['propertyName']
#         moduleName = dossierConfig['moduleName']
#         aliasName = dossierConfig['aliasName']
#         configDtl = dossierConfig['configDtl']
#         isRequired = configDtl['isRequired']
#         if isRequired == 1:
#             # print(moduleName, aliasName, propertyName)
#             num = num + 1
#             propertyNameList.append(propertyName)
# # print(num)
# num2 = 0
# propertyName2List = []
# with open("test2.json", "r", encoding="utf-8") as f:
#     resp = f.read()
# respJson = json.loads(resp)
# data = respJson
# for d in data:
#     propertyName = d['propertyName']
#     moduleName = d['moduleName']
#     aliasName = d['aliasName']
#     # print(moduleName, aliasName, propertyName)
#     num2 = num2 + 1
#     propertyName2List.append(propertyName)
#
# print(propertyNameList)
# print(len(propertyNameList))
# print(propertyName2List)
# print(len(propertyName2List))
# print([i for i in propertyNameList if i not in propertyName2List])
import re
import time

# print(re.findall("(\d\d\d\d-\d+-\d+ \d+:\d+:\d+\.\d+)", '2022-09-28 00:00:00.000'))

RM = """        <id column="ID" jdbcType="VARCHAR" property="id" />
    <result column="NURSE_ID" jdbcType="VARCHAR" property="nurseId" />
    <result column="AUDIT_STATUS" jdbcType="DECIMAL" property="auditStatus" />
    <result column="TITLE" jdbcType="VARCHAR" property="title" />
    <result column="AUTHOR" jdbcType="VARCHAR" property="author" />
    <result column="PUBLISH_DATE" jdbcType="TIMESTAMP" property="publishDate" />
    <result column="ARTICLE_LEVEL" jdbcType="VARCHAR" property="articleLevel" />
    <result column="PERIODICAL" jdbcType="VARCHAR" property="periodical" />
    <result column="YEAR" jdbcType="DECIMAL" property="year" />
    <result column="UNIT_ID" jdbcType="VARCHAR" property="unitId" />
    <result column="URL" jdbcType="VARCHAR" property="url" />
    <result column="AUTHOR_UNIT" jdbcType="VARCHAR" property="authorUnit" />
    <result column="AUTHOR_TITLE" jdbcType="VARCHAR" property="authorTitle" />
    <result column="AUTHOR_LEVEL" jdbcType="VARCHAR" property="authorLevel" />
    <result column="EDIT_STATUS" jdbcType="VARCHAR" property="editStatus" />
    <result column="VALID_FLAG" jdbcType="DECIMAL" property="validFlag" />
    <result column="CREATE_ID" jdbcType="VARCHAR" property="createId" />
    <result column="CREATE_TIME" jdbcType="TIMESTAMP" property="createTime" />
    <result column="UPDATE_ID" jdbcType="VARCHAR" property="updateId" />
    <result column="UPDATE_TIME" jdbcType="TIMESTAMP" property="updateTime" />"""
sql = ""
for i in re.findall("column=\"(.*?)\" .*", RM):
    sql = sql + i+", "
# print(sql)


blockIds = """INSERT INTO MY_TABLE(ID) VALUES ('c398a58717c74226be88c7c67591798e');
INSERT INTO MY_TABLE(ID) VALUES ('633ed888c4864948b968764bcab5256d');
INSERT INTO MY_TABLE(ID) VALUES ('1121a6df7fbd4a328b4fa28ba268d978');
INSERT INTO MY_TABLE(ID) VALUES ('d878f221a9a5415785c80e78409e741e');
INSERT INTO MY_TABLE(ID) VALUES ('5e0a7883e4ad48118c430e5fca6208e7');
INSERT INTO MY_TABLE(ID) VALUES ('a4c588c4b25c47929be2d2537b63f96d');
INSERT INTO MY_TABLE(ID) VALUES ('123dbc3e3b9449b2bedfcdc5706a1787');
INSERT INTO MY_TABLE(ID) VALUES ('3e0aa006cff24050a2f35eea9b10d91a');
INSERT INTO MY_TABLE(ID) VALUES ('98dbb63a20ca4eac8b0c9143042d8530');
INSERT INTO MY_TABLE(ID) VALUES ('151e2fe200f44ef69fa991ffdb3b13d3');
INSERT INTO MY_TABLE(ID) VALUES ('894bca29b3284ea1b130968d1f8387b2');"""

# for i in re.findall("VALUES \\('(.*?)'\\)", blockIds):
#     print(i)
import uuid
# for i in ('a9184b5cd4e14ea7ab1d64c863df293b', '7d1967f8635a48e6ba8c36edba3f006b', '9602b6a5cd0c4cd0b978af5bfcd143fe', '00f46dfc1a0144c88034c26b698ca07b'):
#     for j in re.findall("VALUES \\('(.*?)'\\)", blockIds):
#         id = str(uuid.uuid4()).replace("-", "")
#         time.sleep(0.3)
#         print(f"INSERT INTO NURSE_CONFIG_NQA_BLOCK_MAP (ID, BLOCK_ID, NQA_GROUP_ID, SORT, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID) VALUES ('{id}', '{j}', '{i}', null, null, 1, TO_DATE('2024-09-09 16:56:39', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('2024-09-09 16:56:39', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110');")

#
# for i in ('a9184b5cd4e14ea7ab1d64c863df293b', '7d1967f8635a48e6ba8c36edba3f006b', '9602b6a5cd0c4cd0b978af5bfcd143fe', '00f46dfc1a0144c88034c26b698ca07b'):
#     id = str(uuid.uuid4()).replace("-", "")
#     time.sleep(0.3)
#     print(f"INSERT INTO NURSE_CONFIG_NQA_BLOCK_MAP (ID, BLOCK_ID, NQA_GROUP_ID, SORT, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID) VALUES ('{id}', '3b847a3e2184419e95d1ac951f96d3c2', '{i}', null, null, 1, TO_DATE('2024-09-09 16:56:39', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('2024-09-09 16:56:39', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110');")
#


print("province".upper())