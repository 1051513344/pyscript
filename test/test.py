
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

