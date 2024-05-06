

columns = """    <sql id="Base_Column_List">
        ID, BUSINESS_TYPE, ANNUAL, TIME_TYPE, WARD_ID, WARD_NAME, RESPONSIBLE_ID, RESPONSIBLE_NAME, STATUS,
        CREATE_ID, CREATE_TIME, UPDATE_ID, UPDATE_TIME, VALID_FLAG, WRITE_BY
    </sql>"""



if __name__ == "__main__":

    alias_columns = '    <sql id="Alias_Column_List">'
    alias_columns = alias_columns + "\n        "

    for row in columns.split("\n")[1:-1]:
        line = row.replace("        ", "")
        for column in line.split(","):
            if column != "":
                alias_columns = alias_columns + "qt." + column.strip() + ", "
            else:
                alias_columns = alias_columns + "\n        "
    alias_columns = alias_columns[:-2] + "\n    </sql>"
    print(alias_columns)
