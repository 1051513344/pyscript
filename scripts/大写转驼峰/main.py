
import re

def name_convert_to_camel(name: str) -> str:
    """下划线转驼峰"""
    contents = re.findall('_[a-z]+', name)
    for content in set(contents):
        name = name.replace(content, content[1:].title())
    return name


def name_convert_to_snake(name: str) -> str:
    """驼峰转下划线"""
    if re.search(r'[^_][A-Z]', name):
        name = re.sub(r'([^_])([A-Z][a-z]+)', r'\1_\2', name)
        return name_convert_to_snake(name)
    return name.lower()


def name_convert(name: str) -> str:
    """驼峰式命名和下划线式命名互转"""
    is_camel_name = True  # 是否为驼峰式命名
    if re.match(r'[a-z][_a-z]+$', name):
        is_camel_name = False
    elif re.match(r'[a-zA-Z]+$', name) is None:
        raise ValueError(f'Value of "name" is invalid: {name}')
    return name_convert_to_snake(name) if is_camel_name else name_convert_to_camel(name)
if __name__ == "__main__":

    # text = """<ACCESSTIME></ACCESSTIME>--ACCESSTIME
    #             <ANESTHESIA>冯娟娟</ANESTHESIA>--ANESTHESIA
    #             <ANESTHESIA_BEGINTIME>2023-11-20 08:55:00</ANESTHESIA_BEGINTIME>--ANESTHESIA_BEGINTIME
    #             <ANESTHESIA_ENDTIME>2023-11-20 10:15:00</ANESTHESIA_ENDTIME>--ANESTHESIA_ENDTIME
    #             <BLOOD_IN></BLOOD_IN>--BLOOD_IN
    #             <BLOOD_OUT></BLOOD_OUT>--BLOOD_OUT
    #             <END_DATE_TIME>2023-11-20 10:08:00</END_DATE_TIME>--END_DATE_TIME
    #             <FIRSTAS>吉九威</FIRSTAS>--FIRSTAS
    #             <IN_DATE_TIME>2023-11-20 08:45:00</IN_DATE_TIME>--IN_DATE_TIME
    #             <LEAVETIME></LEAVETIME>--LEAVETIME
    #             <OPERATING_ROOM>麻醉手术科</OPERATING_ROOM>--OPERATING_ROOM
    #             <OPERATING_ROOM_NAME>08间</OPERATING_ROOM_NAME>--OPERATING_ROOM_NAME
    #             <OPERATING_ROOM_NO>8</OPERATING_ROOM_NO>--OPERATING_ROOM_NO
    #             <OPERATIONDATE>2023-11-20</OPERATIONDATE>
    #             <OPER_CODE>51.2300</OPER_CODE>--OPER_CODE
    #             <OPER_DIAGNOSIS>15866^胆囊结石</OPER_DIAGNOSIS>--OPER_DIAGNOSIS
    #             <OPER_ID>1</OPER_ID>--OPER_ID
    #             <OPER_NAME>腹腔镜下胆囊切除术</OPER_NAME>--OPER_NAME
    #             <OPER_QUANTUM></OPER_QUANTUM>--OPER_QUANTUM
    #             <OPER_TYPE>择期</OPER_TYPE>--OPER_TYPE
    #             <OUT_DATE_TIME>2023-11-20 10:15:00</OUT_DATE_TIME>--OUT_DATE_TIME
    #             <PLANNING_BEGINTIME>2023-11-20</PLANNING_BEGINTIME>--PLANNING_BEGINTIME
    #             <SECONDAS></SECONDAS>--SECONDAS
    #             <SORTNO>1</SORTNO>--SORTNO
    #             <SSZT>术毕</SSZT>--SSZT
    #             <START_DATE_TIME>2023-11-20 09:17:00</START_DATE_TIME>--START_DATE_TIME
    #             <SURGEON>张勇刚</SURGEON>--SURGEON
    #             <WOUND_GRADE>1类切口</WOUND_GRADE>--WOUND_GRADE
	# 			<ANESTHESIA_METHOD></ANESTHESIA_METHOD>--ANESTHESIA_METHOD"""
    # for node in text.split("\n"):
    #     # print("@XmlElement(required = true, nillable = true)")
    #     # print("public String "+name_convert(re.findall("<(.*?)>.*</", node)[0].lower()) + ";", "\n")
    #
    #     # print("patientInfo."+name_convert(re.findall("<(.*?)>.*</", node)[0].lower())+" = "+ f'e.elementText("{re.findall("<(.*?)>.*</", node)[0]}");')
    #     print("operation."+name_convert(re.findall("<(.*?)>.*</", node)[0].lower())+" = "+ f'e.elementText("{re.findall("<(.*?)>.*</", node)[0]}");')



    text = """               <ANESTHESIA_ASSISTANT/>                                
               <ANESTHESIA_DOCTOR>20190211</ANESTHESIA_DOCTOR>         --------麻醉医师工号
               <ANESTHESIA_METHOD>全身麻醉</ANESTHESIA_METHOD>          --------麻醉方法
               <APPLY_NO/>
               <AUDITOR_BY/>
               <BLOOD_TRAN_DOCTOR/>
               <EMERGENCY_INDICATOR>N</EMERGENCY_INDICATOR>            ---------急诊标识（N-否/Y-是）
               <ENTERED_BY/>
               <FIRST_ASSISTANT/>
               <FIRST_OPERATION_NURSE/>
               <FIRST_SUPPLY_NURSE>王燕</FIRST_SUPPLY_NURSE>           ----------第一供应护士
               <FOURTH_ANESTHESIA_ASSISTANT/>
               <FOURTH_ASSISTANT/>
               <INCISION>2类切口</INCISION>                            ------------手术切口等级
               <ISOLATION_INDICATOR/>
               <NOTES_ON_OPERATION>胃窦粘膜下肿物挖除术[ESE]</NOTES_ON_OPERATION>   ------备注
               <OPERATING_ROOM_CODE>0401</OPERATING_ROOM_CODE>                    ------手术室编码
               <OPERATING_ROOM_NAME>麻醉手术科</OPERATING_ROOM_NAME>               ------手术室名称
               <OPERATING_ROOM_NO>16间</OPERATING_ROOM_NO>                        ------手术室间号
               <OPERATION_CODE>43.4107</OPERATION_CODE>                           ------手术编码
               <OPERATION_LEVEL>四级</OPERATION_LEVEL>                            -------手术分级
               <OPERATION_NAME>内镜下胃黏膜下剥离术[ESD]</OPERATION_NAME>          --------手术名称
               <OPERATION_STATUS>术毕</OPERATION_STATUS>                          --------手术状态
               <PATIENT_CONDITION/>
               <PREOPERATIVE_DIAGNOSIS>胃肿物</PREOPERATIVE_DIAGNOSIS>            -------术前诊断
               <PREOPERATIVE_DIAGNOSIS_CODE>R65.000</PREOPERATIVE_DIAGNOSIS_CODE>     -------诊断编码
               <REQ_DATE/>
               <SCHEDULE_DATE>2023-11-22 14:30:00</SCHEDULE_DATE>                    --------手术排班时间
               <SCHEDULE_ID>24224</SCHEDULE_ID>                              -------------手术单号        
               <SECOND_ANESTHESIA_ASSISTANT/>
               <SECOND_ANESTHESIA_DOCTOR/>
               <SECOND_ASSISTANT/>
               <SECOND_OPERATION_NURSE/>
               <SECOND_SUPPLY_NURSE/>
               <SEQUENCE>2</SEQUENCE>                                        -------------手术台次
               <SURGEON>1462</SURGEON>                                       -------------手术医生工号
               <THIRD_ANESTHESIA_ASSISTANT/>
               <THIRD_ANESTHESIA_DOCTOR/>
               <THIRD_ASSISTANT/>
               <THIRD_SUPPLY_NURSE/>"""
    for node in text.split("\n"):
        find_result = re.findall("<(.*?)>.*</", node)
        if len(find_result) == 0:
            find_result = re.findall("<(.*?)/>", node)
        mean_result = re.findall("--(.*)", node)
        if len(mean_result) > 0:
            print("/**")
            print(" * "+mean_result[0].replace("-", "").strip())
            print("*/")
        print("@XmlElement(required = true, nillable = true)")
        print("public String "+name_convert(find_result[0].lower()) + ";", "\n")
        # print("patientInfo."+name_convert(find_result[0].lower())+" = "+ f'e.elementText("{find_result[0]}");')
        # print("patientInfo."+name_convert(find_result[0].lower())+" = "+ f'operElement.element("PatInfo").elementText("{find_result[0]}");')
        # print("operation."+name_convert(find_result[0].lower())+" = "+ f'operationElement.elementText("{find_result[0]}");')
        # print("operation."+name_convert(find_result[0].lower())+" = "+ f'e.elementText("{find_result[0]}");')
