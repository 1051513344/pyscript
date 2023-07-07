from sql.query.queryDataFunc import QueryDB




if __name__ == "__main__":
    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "************"
    db = "ucmed2-base"
    charset = "utf8"
    table_name = "turn_inter_std_plan"
    # 获取需要导出的数据
    q = QueryDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )

    results = q.queryByCustom("SELECT moduleid, name, perms FROM Menus WHERE moduleid IN ('turn','trainee','futuredoctorapp') AND menu_type = 'F'")
    for result in results:
        if result['perms'] is not None:
            moduleid = result['moduleid']
            name = result['name']
            perms = result['perms']
            perms_split = result['perms'].split(":")
            if len(perms_split) > 1:
                for i in range(len(perms_split[:-1])):
                    perms_split[i] = perms_split[i].upper()
                perms_split[-1] = perms_split[-1][0].upper() + perms_split[-1][1:]
            emum = moduleid.upper() + "_" + "_".join(perms_split)
            print(f'{emum}("{moduleid}", "{name}" , "{perms}"),')
