
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

    year_dict = {
        "517": 2,
        "518": 2,
        "519": 1,
    }
    stu_id_set = []
    result = q.queryByCustom("select * from turn_inter_std_plan where verification_years is not null and status = 0 and stu_id not in (select std_id from turn_personal_evaluate )")
    # print(result)
    for r in result:
        if r['verification_years'] in year_dict:
            stu_id = r['stu_id']
            base_id = r['base_id']
            year_flag = year_dict[r['verification_years']]
            base_status = 0
            teachoffice_status = 0
            # print(stu_id)
            # print(base_id)
            # print(year_flag)
            if stu_id not in stu_id_set:
                for i in range(1, int(year_flag)+1):
                    print(f"insert into turn_personal_evaluate (std_id, base_id, year_flag, std_status, base_status, teachoffice_status) values ({stu_id}, {base_id}, {i}, 0, {base_status}, {teachoffice_status});")
                stu_id_set.append(stu_id)
