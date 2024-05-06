

import pandas as pd


if __name__ == "__main__":

    # with pd.ExcelFile("ViewSS_unsorted.xls") as xls:
    #     df = pd.read_excel(xls, "Sheet1")
    #     for row_index, row in df.iterrows():
    #         # print(row, sep='\n')
    #         CSSID = row[0]
    #         CBRH = row[1]
    #         CXM = row[2]
    #         CKSBM = row[3]
    #         CKSMC = row[4]
    #         DSHSJ = row[5]
    #         DSSSJ = row[6]
    #         BZ = "'{}'".format(row[7]) if str(row[7]) != 'nan' else 'null'
    #         print(f"SELECT '{CSSID}' CSSID, '{CBRH}' CBRH, '{CXM}' CXM, '{CKSBM}' CKSBM, '{CKSMC}' CKSMC, '{DSHSJ}' DSHSJ, '{DSSSJ}' DSSSJ, {BZ} BZ")
    #         print("union all")

    # with pd.ExcelFile("ViewSS_overtime.xls") as xls:
    #     df = pd.read_excel(xls, "Sheet1")
    #     for row_index, row in df.iterrows():
    #         # print(row, sep='\n')
    #         CSSID = row[0]
    #         CBRH = row[1]
    #         CKSBM = row[2]
    #         CKSMC = row[3]
    #         DSHSJ = row[4]
    #         DSSSJ = row[5]
    #         print(f"SELECT '{CSSID}' CSSID, '{CBRH}' CBRH, '{CKSBM}' CKSBM, '{CKSMC}' CKSMC, '{DSHSJ}' DSHSJ, '{DSSSJ}' DSSSJ")
    #         print("union all")

    # with open("疼痛.csv", "r", encoding='utf-8') as f:
    #     source = f.read()
    # with open("view.sql", "w", encoding='utf-8') as f:
    #     createViewSql = ""
    #     for row in source.split("\n")[1:]:
    #         value1 = row.split(",")[0].replace("\"", "'")
    #         value2 = row.split(",")[1].replace("\"", "'")
    #         value3 = row.split(",")[2].replace("\"", "'")
    #         value4 = row.split(",")[3].replace("\"", "'")
    #         value5 = row.split(",")[4].replace("\"", "'")
    #         value6 = row.split(",")[5].replace("\"", "'")
    #         columnSql = f"select  {value1} PATIENT_ID,  {value2}  NAME,  {value3}  WARD_NAME,  {value4}  BED_NO, {value5} NUMBER_VALUE,  to_date({value6} , 'yyyy-mm-dd hh24:mi:ss')  FORM_TIME from dual"
    #         createViewSql = createViewSql + columnSql + "\n"
    #         createViewSql = createViewSql + "union all\n"
    #     f.write(createViewSql)


    with open("4月手术.csv", "r", encoding='utf-8') as f:
        source = f.read()
    columns = source.split("\n")[0].replace('\ufeff', '').split(",")
    # print(columns)
    with open("view.sql", "w", encoding='utf-8') as f:
        createViewSql = ""
        for row in source.split("\n")[1:]:
            columnSql = "select  "
            values = row.split(",")
            if len(values) != 16:
                print(values)
            for c, v in zip(columns, values):
                if "-" and ":" in v:
                    value = "to_date('{}','yyyy-mm-dd hh24:mi:ss')".format(v.replace('"', ""))
                elif "-" in v:
                    value = "to_date('{}','yyyy-mm-dd hh24:mi:ss')".format(v.replace('"', "") + " 00:00:00")
                else:
                    value = v.replace('"', "'")
                # 最后一个字段名
                if c != '"是否复苏"':
                    columnSql = columnSql + value + " " + c.replace('"', "") + ", "
                else:
                    columnSql = columnSql + value + " " + c.replace('"', "")
            # print(columnSql)
            columnSql = columnSql + " from dual"
            # print(columnSql)
            createViewSql = createViewSql + columnSql + "\n"
            createViewSql = createViewSql + "union all\n"
        f.write(createViewSql)





