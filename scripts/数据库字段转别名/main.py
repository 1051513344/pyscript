

columns = """  <sql id="Base_Column_List">
    ID, FORM_TYPE, CHECK_TYPE_ID, CHECK_TYPE_NAME, CHECK_STANDARD_ID, CHECK_STANDARD_NAME, 
    FEEDBACK_NUM, CREATE_ID, CREATE_TIME, UPDATE_ID, UPDATE_TIME, VALID_FLAG,QC_DATA_DETAIL_DICT_ID,
    SERIAL_NUMBER, VERSION, RELEASE_STATUS, RELEASE_TIME, EDITOR_ID, EDITOR_NAME, REVIEWER_ID, REVIEWER_NAME,
    RANGE_TYPE,TOUCH_WARD_IDS,TOUCH_WARD_INFO,TOUCH_DEPT_IDS,UNIT_TYPE,UNIT_ID,QUALIFIED_SCORE,
    STANDARD_TYPE, STANDARD_CATEGORY, SUPPORT_TEST_PAPER,SYSTEM_FLAG,STANDARD_STYLE,INDICATOR_CODE, COLLECT_WAY,
    SPECIAL_TEAM,PATIENT_CHECKUP_FORM,MIN_CHECK_PEOPLE_NUM,
    NURSE_CHECKUP_FORM,NURSE_MIN_CHECK_PEOPLE_NUM,
    SCORING_TYPE,MIN_INS_FREQUENCY,ITEM_PROGRESSION,QC_INDEX_DICT_IDS,OPEN_QC_REQUIREMENTS,QC_REQUIREMENTS_CONTENT
  </sql>"""



if __name__ == "__main__":

    alias_columns = '    <sql id="Alias_Column_List">'
    alias_columns = alias_columns + "\n        "

    for row in columns.split("\n")[1:-1]:
        line = row.replace("        ", "")
        for column in line.split(","):
            if column != "" and column != " ":
                alias_columns = alias_columns + "SF." + column.strip() + ", "
            else:
                alias_columns = alias_columns + "\n        "
    alias_columns = alias_columns[:-2] + "\n    </sql>"
    print(alias_columns)
