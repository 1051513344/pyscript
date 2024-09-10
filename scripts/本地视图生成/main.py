import re




if __name__ == "__main__":

    # 本地虚拟视图生成器

#     sourse = """insert into V_HLGL_TTPG (PATIENT_ID, NAME, WARD_NAME, BED_NO, NUMBER_VALUE, FORM_TIME)
# values ('24039142', '刘本知', '血液内科', '05', '0', to_date('31-03-2024 15:46:44', 'dd-mm-yyyy hh24:mi:ss'));"""
    with open("source.sql", "r", encoding='utf-8') as f:
        sourse = f.read()
    virtualViewName = "v_yh_hl_duty"
    createViewSql = "create view {} as {}"
    for row in sourse.split("\n"):
        if row.startswith("INSERT INTO "):
            column = row.replace(f"INSERT INTO {virtualViewName}(", "").replace(")","").strip()
            break
    # print(column)
    columns = column.split(",")
    columnSql = ""
    dateTimeColumn = ['term_of_validity']
    for row in sourse.split("\n"):
        if row.startswith(" VALUES ") or row.startswith("VALUES "):
            columnSql = columnSql + "select "
            value = row.replace("VALUES (", "").strip()
            values = []
            tempValue = ""
            for v in value:
                # oracle日期格式
                if tempValue.startswith(" to_date"):
                    tempValue = tempValue + v
                    if tempValue.endswith(")"):
                        # print(tempValue)
                        values.append(tempValue)
                        tempValue = ""
                elif len(re.findall("('\d\d\d\d-\d+-\d+ \d+:\d+:\d+\.\d{3}')", tempValue)) > 0:
                    # sqlServer日期格式
                    datetimeStr = re.findall("('\d\d\d\d-\d+-\d+ \d+:\d+:\d+\.\d{3}')", tempValue)[0]
                    tempValue = f'CAST({datetimeStr} AS DATETIME)'
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
                if (f'{c}'.strip() in dateTimeColumn or f'{c}'.strip().endswith("_date") or f'{c}'.strip().endswith("_time")) and 'CAST' not in v:
                    # sqlServer日期格式
                    columnSql = columnSql + f" CAST({v} AS DATETIME) {c},"
                else:
                    columnSql = columnSql + f" {v} {c},"
            columnSql = columnSql[:-1] + "\nunion all\n"
            # print(columnSql)
    # print(columnSql)
    createViewSql = createViewSql.format(virtualViewName, columnSql[:-11])
    with open("view.sql", "w", encoding='utf-8') as f:
        f.write(createViewSql)
    # print(createViewSql)






