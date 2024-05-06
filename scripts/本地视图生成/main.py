




if __name__ == "__main__":

    # 本地虚拟视图生成器

    sourse = """insert into V_HLGL_TTPG (PATIENT_ID, NAME, WARD_NAME, BED_NO, NUMBER_VALUE, FORM_TIME)
values ('24039142', '刘本知', '血液内科', '05', '0', to_date('31-03-2024 15:46:44', 'dd-mm-yyyy hh24:mi:ss'));"""

    virtualViewName = "V_HLGL_TTPG"
    createViewSql = "create view {} as {}"
    for row in sourse.split("\n"):
        if row.startswith("insert into "):
            column = row.replace("insert into V_HLGL_TTPG (", "").replace(")","").strip()
            break
    # print(column)
    columns = column.split(",")
    columnSql = ""
    for row in sourse.split("\n"):
        if row.startswith("values "):
            columnSql = columnSql + "select "
            value = row.replace("values (", "").strip()
            values = []
            tempValue = ""
            for v in value:
                if tempValue.startswith(" to_date"):
                    tempValue = tempValue + v
                    if tempValue.endswith(")"):
                        # print(tempValue)
                        values.append(tempValue)
                        tempValue = ""
                else:
                    if v == ",":
                        if tempValue != "":
                            # print(tempValue)
                            values.append(tempValue)
                        tempValue = ""
                    else:
                        tempValue = tempValue + v
                        if tempValue.endswith(");"):
                            tempValue = tempValue.replace(");", "")
                            values.append(tempValue)

            for c,v in zip(columns, values):
                columnSql = columnSql + f" {v} {c},"
            columnSql = columnSql[:-1] + " from dual\nunion all\n"
            # print(columnSql)
    # print(columnSql)
    createViewSql = createViewSql.format(virtualViewName, columnSql)
    with open("view.sql", "w", encoding='utf-8') as f:
        f.write(createViewSql)
    # print(createViewSql)






