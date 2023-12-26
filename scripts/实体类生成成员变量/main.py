
from scripts.util import convertUtil


source = """
    ID                  VARCHAR2(80 char)  
    CODE                VARCHAR2(20),
    NAME                VARCHAR2(20),
    TYPE                CHAR,
    WARD_CODE           VARCHAR2(20),
    WARD_NAME           VARCHAR2(80),
    SET_TIMES           NUMBER,
    PLAN_TYPE           CHAR,
    REASON              VARCHAR2(400),
    PATIENT_UID         VARCHAR2(60),
    PATIENT_NAME        VARCHAR2(40),
    SET_DATE            DATE,
    CHECK_DATE          DATE,
    CHECK_BY            VARCHAR2(40),
    CHECK_NAME          VARCHAR2(40),
    TAKE_OUT_TYPE       VARCHAR2(20),
    TAKE_OUT_TIME       DATE,
    TAKE_OUT_REASON     VARCHAR2(400),
    TAKE_OUT_AUDIT_BY   VARCHAR2(40),
    TAKE_OUT_AUDIT_NAME VARCHAR2(40),
    IS_VALID            NUMBER(1),
    CREATE_BY           VARCHAR2(40),
    CREATE_NAME         VARCHAR2(40),
    CREATE_DATE         DATE,
    LAST_UPDATED_BY     VARCHAR2(40),
    LAST_UPDATED_NAME   VARCHAR2(40),
    LAST_UPDATED_DATE   DATE
"""
dict = """
comment on column MCS_DUCT_INFO.CODE is '导管编码'
/

comment on column MCS_DUCT_INFO.NAME is '导管名称'
/

comment on column MCS_DUCT_INFO.TYPE is '1、本科室置管；2、带入'
/

comment on column MCS_DUCT_INFO.WARD_CODE is '置管科室编码'
/

comment on column MCS_DUCT_INFO.WARD_NAME is '置管科室名称'
/

comment on column MCS_DUCT_INFO.SET_TIMES is '置管次数：1、首次；'
/

comment on column MCS_DUCT_INFO.PLAN_TYPE is '1、计划性；2、非计划性（须填原因）'
/

comment on column MCS_DUCT_INFO.REASON is '非计划性原因'
/

comment on column MCS_DUCT_INFO.PATIENT_UID is '病人uid'
/

comment on column MCS_DUCT_INFO.PATIENT_NAME is '病人name'
/

comment on column MCS_DUCT_INFO.SET_DATE is '置管时间'
/

comment on column MCS_DUCT_INFO.CHECK_DATE is '核对时间'
/

comment on column MCS_DUCT_INFO.CHECK_BY is '核对人工号'
/

comment on column MCS_DUCT_INFO.CHECK_NAME is '核对人'
/

comment on column MCS_DUCT_INFO.TAKE_OUT_TYPE is '拔管类型'
/

comment on column MCS_DUCT_INFO.TAKE_OUT_TIME is '拔管时间'
/

comment on column MCS_DUCT_INFO.TAKE_OUT_REASON is '拔管原因'
/

comment on column MCS_DUCT_INFO.TAKE_OUT_AUDIT_BY is '拔管审核人工号'
/

comment on column MCS_DUCT_INFO.TAKE_OUT_AUDIT_NAME is '拔管审核人'
/

comment on column MCS_DUCT_INFO.IS_VALID is '1、正常；0、删除'
/

comment on column MCS_DUCT_INFO.CREATE_BY is '创建人工号'
/

comment on column MCS_DUCT_INFO.CREATE_NAME is '创建人'
/

comment on column MCS_DUCT_INFO.CREATE_DATE is '创建时间'
/

comment on column MCS_DUCT_INFO.LAST_UPDATED_BY is '最后更新人工号'
/

comment on column MCS_DUCT_INFO.LAST_UPDATED_NAME is '最后更新人'
/

comment on column MCS_DUCT_INFO.LAST_UPDATED_DATE is '最后更新时间'
/

"""




if __name__ == "__main__":

    property_dict = {}
    for i in dict.split("\n"):
        if "." in i:
            property = i.split(".")[1].split(" ")[0]
            value = i.split(".")[1].split(" ")[2]
            property_dict[property] = value

    Base_Column_List = ""

    for i in source.split("\n"):
        if i != "":
            property = ""
            for index in i[4:]:
                if index == " ":
                    break
                property = property + index
            column = property
            property = convertUtil.name_convert(property.lower())
            # if property == "id":
            #     print('@Id')
            #     print('@ApiModelProperty(name = "id" , value = "主键")')
            #     print('@Column(name = "ID")')
            #     print('private String id;\n')
            # else:
            #         print(f'@ApiModelProperty(name = "{property}" , value = "{property_dict[column] if column in property_dict else ""}")')
            #         print(f'@Column(name = "{column}")')
            #         print(f'private String {property};\n')
            # print(f'<result column="{column}" jdbcType="VARCHAR" property="{property}" />')
            # Base_Column_List = Base_Column_List + column + ","
    # print(Base_Column_List[:-1])

