import json


def gen1():
    s = """INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('staffOnLeave', 'string', '病、事假、迟到姓名');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('prominentCase', 'string', '突出事例');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('newTechnology', 'string', '新技术');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('teach', 'string', '教学');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('researchAndPapers', 'string', '科研、论文');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('nurseNum', 'int', '护士数');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('severeCaseNum', 'int', '重症数');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('commendatoryLetter', 'int', '表扬信');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('criticismLetter', 'int', '批评信');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('nursingRounds', 'int', '护理查房');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('errorNum', 'int', '差错');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('rotatingNurse', 'string', '轮入护士');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('accidentNum', 'int', '事故');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('alternateNurse', 'string', '轮出护士');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('learningAndActivities', 'string', '业务学习、病房活动');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('jobImprovement', 'string', '工作改进');
INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('suggestion', 'string', '科内存在问题，对护理部建议，其他情况');"""

    for i in s.split("\n"):
        field = i.replace("INSERT INTO HLZK_DALIANFUYI.NURSE_HEAD_WORK_SUMMARY_FIELD_CONFIG (FIELD_NAME, FIELD_TYPE, FIELD_REMARK) VALUES ('", "").replace("');", "")
        name = field.split("', '")[0]
        type = field.split("', '")[1]
        remark = field.split("', '")[2]
        print("    /**\n     * {}\n     */".format(remark))
        if type == 'int':
            print("    private Integer {};".format(name)+"\n")
        if type == 'string':
            print("    private String {};".format(name)+"\n")

from scripts.大写转驼峰.main import name_convert
def gen2():
    ddl = """    ID           VARCHAR2(32) not null
        constraint NURSE_HEAD_WORK_SUMMARY_RECORD_PK
            primary key,
    BASE_INFO_ID VARCHAR2(32) not null,
    FIELD_NAME   VARCHAR2(32),
    STRING_VALUE VARCHAR2(2000),
    INT_VALUE    NUMBER"""

    for i in ddl.split("\n"):
        if i == "" or i == "constraint" or i == "primary":
            continue
        field = [x for x in i.split(" ") if x !=''][0]
        if "NUMBER" in i:
            print("private Integer {};\n".format(name_convert(field.lower())))
        elif "VARCHAR2" in i:
            print("private String {};\n".format(name_convert(field.lower())))
        elif "DATE" in i:
            print("private Date {};\n".format(name_convert(field.lower())))

def gen3():
    ddl = """    ID           VARCHAR2(32) not null
        constraint NURSE_HEAD_WORK_SUMMARY_RECORD_PK
            primary key,
    BASE_INFO_ID VARCHAR2(32) not null,
    FIELD_NAME   VARCHAR2(32),
    STRING_VALUE VARCHAR2(2000),
    INT_VALUE    NUMBER"""

    for i in ddl.split("\n"):
        if i == "" or i == "constraint" or i == "primary":
            continue
        field = [x for x in i.split(" ") if x !=''][0]
        if "NUMBER" in i:
            print(f'<result column="{field}" jdbcType="INTEGER" property="{name_convert(field.lower())}" />')
        elif "VARCHAR2" in i:
            print(f'<result column="{field}" jdbcType="VARCHAR" property="{name_convert(field.lower())}" />')
        elif "DATE" in i:
            print(f'<result column="{field}" jdbcType="TIMESTAMP" property="{name_convert(field.lower())}" />')

def gen4():
    ddl = """    ID           VARCHAR2(32) not null
        constraint NURSE_HEAD_WORK_SUMMARY_RECORD_PK
            primary key,
    BASE_INFO_ID VARCHAR2(32) not null,
    FIELD_NAME   VARCHAR2(32),
    STRING_VALUE VARCHAR2(2000),
    INT_VALUE    NUMBER"""
    print('  <sql id="Base_Column_List">')
    baseColumn = "    "
    for i in ddl.split("\n"):
        if i == "" or "constraint" in i or "primary" in i:
            continue
        field = [x for x in i.split(" ") if x !=''][0]
        baseColumn = baseColumn + f" {field},"
    print(baseColumn[:-1])
    print('  </sql>')

def gen5():
    dict = {}
    property = """    private String wardId;
    private String wardName;
    private String headNurseSigned;
    private int year;
    private int quarter;
    private String staffOnLeave;
    private String prominentCase;
    private String newTechnology;
    private String teach;
    private String researchAndPapers;
    private Integer nurseNum;
    private Integer severeCaseNum;
    private Integer commendatoryLetter;
    private Integer criticismLetter;
    private Integer nursingRounds;
    private Integer errorNum;
    private String rotatingNurse;
    private Integer accidentNum;
    private String alternateNurse;
    private String learningAndActivities;
    private String jobImprovement;
    private String suggestion;"""
    for i in property.split("\n"):
        if i.startswith("    private "):
            p = i.split(" ")[-1].replace(";", "")
            dict[p] = "2"
    print(json.dumps(dict))


if __name__ == "__main__":

    # gen2()
    # gen3()
    # gen4()
    gen5()
