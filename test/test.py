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
#             addHeader("��Ů�ֲ�",4000);
#         }
#         int titleHeaderSize = 7;
#         for (int i = 0; i < titleHeaderSize; i++) {
#             addHeader("ְ�Ʒֲ�",4000);
#         }
#         int levelHeaderSize = 7;
#         for (int i = 0; i < levelHeaderSize; i++) {
#             addHeader("�㼶�ֲ�",4000);
#         }
#         int positionHeaderSize = 12;
#         for (int i = 0; i < positionHeaderSize; i++) {
#             addHeader("ְ��ֲ�",4000);
#         }
#         int ageHeaderSize = 7;
#         for (int i = 0; i < ageHeaderSize; i++) {
#             addHeader("����ηֲ�",4000);
#         }
#         int eduHeaderSize = 9;
#         for (int i = 0; i < eduHeaderSize; i++) {
#             addHeader("ѧ���ֲ�",4000);
#         }
#         int postHeaderSize = 3;
#         for (int i = 0; i < postHeaderSize; i++) {
#             addHeader("��λ���ֲ�",4000);
#         }
#         int natureHeaderSize = 11;
#         for (int i = 0; i < natureHeaderSize; i++) {
#             addHeader("ְ�����ʷֲ�",4000);
#         }
#         int workYearHeaderSize = 7;
#         for (int i = 0; i < workYearHeaderSize; i++) {
#             addHeader("�������޷ֲ�",4000);
#         }
#         int specialtyHeaderSize = 6;
#         for (int i = 0; i < specialtyHeaderSize; i++) {
#             addHeader("ר�ƻ�ʿ�ֲ�",4000);
#         }
#         int hosYearHeaderSize = 7;
#         for (int i = 0; i < hosYearHeaderSize; i++) {
#             addHeader("��Ժ����",4000);
#         }
#         int tcmHeaderSize = 3;
#         for (int i = 0; i < tcmHeaderSize; i++) {
#             addHeader("��ҽԺУ�ֲ�",4000);
#         }
#         int professionHeaderSize = 3;
#         for (int i = 0; i < professionHeaderSize; i++) {
#             addHeader("רҵ���",4000);
#         }
#         int statusHeaderSize = 2;
#         for (int i = 0; i < statusHeaderSize; i++) {
#             addHeader("��ְ״̬",4000);
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
# with open("../scripts/mybatisLogDDL����ֶγ���/DDL.sql", "r") as f:
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
# with open('../scripts/mybatisLogDDL����ֶγ���/test.txt', "r", encoding='utf-8') as f:
#     x = f.read()
# with open('../scripts/mybatisLogDDL����ֶγ���/text2.txt', "r", encoding='utf-8') as f:
#     y = f.read()
# l = x.split(", ")
# l2 = y.split(", ")
# for i1,i2 in zip(l, l2):
#     print(i1,"\t"+ i2,"\t"+ str(len(i2.replace("(String)", "").replace("(Integer)", "").replace("(Double)", ""))) if i2 is not None and i2 != 'null' else 0, cdict[i1] if i1 in cdict else '0', "--------------------------------------------" if (len(i2.replace("(String)", "").replace("(Integer)", "").replace("(Double)", "")) if i2 is not None and i2 != 'null' else 0) > (int(cdict[i1]) if i1 in cdict else 0) else "")
#
# with open('../scripts/mybatisLogDDL����ֶγ���/text3.txt', "r", encoding='utf-8') as f:
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
print(re.findall("(\d\d\d\d-\d+-\d+ \d+:\d+:\d+\.\d+)", '2022-09-28 00:00:00.000'))