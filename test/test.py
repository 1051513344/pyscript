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
import  re
import  uuid
s = """INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('5F2E88438F664F01A958B174B3F91665', 'BFE1C829716649C599A818F995877BCD', 'Ժ��ѧϰ��¼', 4, 1, 1, 0, 0, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'IN_HOSPITAL_LEARNING_RECORD', 'SHORT_TERM_LEARNING', null, null, null, null, null, null, null, 1, null, null, 'IN_HOSPITAL_LEARNING_RECORD', null, null, 'Ժ��ѧϰ��¼', 0, 0, 0, 0, 0, 100, 2, 4, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('232F628B135346DD91238741A5415AFB', '5F2E88438F664F01A958B174B3F91665', '��ѵ���', 13, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'remark', 'IN_HOSPITAL_LEARNING_RECORD', 1, 'PEIXUNJIEGUO', null, null, 1, '��ѵ���', 0, 1, null, null, 'remarkStr', null, null, '��ע', 1, 1, 0, 1, 0, 100, 2, 13, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('99398B5D1C654560A12354142E9704F7', '5F2E88438F664F01A958B174B3F91665', '�ص�', 8, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'address', 'IN_HOSPITAL_LEARNING_RECORD', 3, null, null, null, 1, null, 0, 1, null, null, 'address', null, null, '�ص�', 1, 1, 0, 0, 0, 100, 2, 8, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('8A47BA8FA83E409E8123C7A2961B07F0', '5F2E88438F664F01A958B174B3F91665', 'ѧʱ���', 12, 1, 1, 0, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'classHourType', 'IN_HOSPITAL_LEARNING_RECORD', 1, 'NURSE_CLASS_HOURS_TYPE', null, null, 1, 'ѧʱ���', 1, 1, null, null, 'classHourTypeStr', null, null, 'ѧʱ���', 0, 1, 0, 1, 0, 100, 2, 12, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('985F191A98A2410F9123413560F448F9', '5F2E88438F664F01A958B174B3F91665', '��������', 7, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'endDate', 'IN_HOSPITAL_LEARNING_RECORD', 5, null, null, null, 4, null, 0, 1, null, null, 'endDate', null, null, '��������', 0, 1, 0, 1, 0, 100, 2, 7, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('73A5BD8C146244008123E76982C0153E', '5F2E88438F664F01A958B174B3F91665', '��ʼ����', 6, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'startDate', 'IN_HOSPITAL_LEARNING_RECORD', 5, null, null, null, 4, null, 1, 1, null, null, 'startDate', null, null, '��ʼ����', 1, 1, 0, 1, 0, 100, 2, 6, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('CEF9ED9779864850B1232CE774CB7D11', '5F2E88438F664F01A958B174B3F91665', 'ѧϰ����', 5, 1, 1, 0, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'studyContent', 'IN_HOSPITAL_LEARNING_RECORD', 4, null, null, null, 1, null, 0, 1, null, null, 'studyContent', null, null, 'ѧϰ����', 0, 1, 0, 1, 0, 100, 2, 5, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('FEF777DA2F614BA29123C76B0D18FD02', '5F2E88438F664F01A958B174B3F91665', '��Ŀ���', 0, 1, 1, 0, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'projectCode', 'IN_HOSPITAL_LEARNING_RECORD', 3, null, null, null, 1, null, 0, 1, null, null, 'projectCode', null, null, '��Ŀ���', 1, 1, 0, 1, 0, 100, 2, 0, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('87175C61C1E942AB91231C8CE406CEF9', '5F2E88438F664F01A958B174B3F91665', '���', 1, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'year', 'IN_HOSPITAL_LEARNING_RECORD', 3, null, null, null, 2, null, 1, 1, null, null, 'year', null, null, '���', 1, 1, 0, 1, 0, 100, 2, 1, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('C0FFE0EFD3A44DB88123FBC9080832C4', '5F2E88438F664F01A958B174B3F91665', 'ѧ��', 9, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'credit', 'IN_HOSPITAL_LEARNING_RECORD', 3, null, null, null, 3, null, 1, 1, null, null, 'credit', null, null, 'ѧ��', 1, 1, 0, 1, 0, 100, 2, 9, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('B521476A8EAD4ECB91231CF38C25CA62', '5F2E88438F664F01A958B174B3F91665', 'ѧ������', 10, 1, 1, 0, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'creditType', 'IN_HOSPITAL_LEARNING_RECORD', 1, 'CREDITS_XUEFENLEIBIE', null, null, 1, 'ѧ�����', 1, 1, null, null, 'creditTypeStr', null, null, 'ѧ������', 1, 1, 0, 1, 0, 100, 2, 10, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('BDB00E2A75C04768B12326EA6BA55357', '5F2E88438F664F01A958B174B3F91665', 'ѧʱ', 11, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'classHour', 'IN_HOSPITAL_LEARNING_RECORD', 3, null, null, null, 3, null, 1, 1, null, null, 'classHour', null, null, 'ѧʱ', 1, 1, 0, 1, 0, 100, 2, 11, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('3FFA0AA4EF84402791233E9D2A8D220D', '5F2E88438F664F01A958B174B3F91665', '����', 14, 1, 1, 0, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'url', 'IN_HOSPITAL_LEARNING_RECORD', 9, null, null, null, 1, null, 0, 1, null, null, 'url', null, null, '����', 0, 1, 0, 0, 0, 100, 2, 14, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('8AV4BA8FA83E409E83D3C7A2961B07YH', '5F2E88438F664F01A958B174B3F91665', '���', 2, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'type', 'IN_HOSPITAL_LEARNING_RECORD', 1, 'LEARNING_RECORD_TYPE', null, null, 1, '���', 1, 1, null, null, 'typeStr', null, null, '���', 1, 1, 0, 1, 0, 100, 2, 2, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('SW2F628B135346DD93C68741A5415AD4', '5F2E88438F664F01A958B174B3F91665', '�γ�����', 3, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'courseName', 'IN_HOSPITAL_LEARNING_RECORD', 4, null, null, null, 1, null, 1, 1, null, null, 'courseName', null, null, '�γ�����', 1, 1, 0, 1, 0, 100, 2, 3, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('BK2F628B135346DD93C68741A5415AM7', '5F2E88438F664F01A958B174B3F91665', '�ڿ���ʦ', 4, 1, 1, 1, 1, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'teacher', 'IN_HOSPITAL_LEARNING_RECORD', 4, null, null, null, 1, null, 0, 1, null, null, 'teacher', null, null, '�ڿ���ʦ', 1, 1, 0, 1, 0, 100, 2, 4, 1, 1, 1, null);
INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('D8A5BD8C1462440085CCE76982C015U0', '5F2E88438F664F01A958B174B3F91665', '����ʱ��', 15, 1, 1, 0, 0, null, 1, TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', TO_DATE('2024-03-04 13:12:01', 'YYYY-MM-DD HH24:MI:SS'), '6b012f0b64164d04955631b8a7073e27', 'curriculumTime', 'IN_HOSPITAL_LEARNING_RECORD', 5, null, null, null, 4, null, 0, 1, null, null, 'curriculumTime', null, null, '����ʱ��', 0, 0, 0, 0, 0, 100, 2, 15, 1, 1, 1, null);"""
pid = "BFE1C829716649C599A818F995877BCD"
parent_id = ""
index = 0
for row in s.split("\n"):
    id_pattern = "VALUES \('(.*?)', "
    parent_id_pattern = "VALUES \('.*?', '(.*?)', "
    id = re.findall(id_pattern, row)[0]
    o_parent_id = re.findall(parent_id_pattern, row)[0]
    new_id = str(uuid.uuid4()).replace("-", "").upper()
    row = row.replace(id, new_id)
    row = row.replace("2024-03-04 13:12:01", "2024-04-28 15:06:13")
    row = row.replace("Ժ��", "������")
    row = row.replace("IN_HOSPITAL_LEARNING_RECORD", "WARD_LEARNING_RECORD")
    if index == 0:
        parent_id = pid
        pid = new_id
    elif index == 1:
        parent_id = pid
    if index > 0:
        row = row.replace(o_parent_id, parent_id)
    index = index + 1
    print(row)

