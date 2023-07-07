from sql.query.queryDataFunc import QueryDB

if __name__ == "__main__":

    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "************"
    db = "ucmed2-base"
    charset = "utf8mb4"
    table_name = "turn_plan_evaluation"

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

    result = q.queryAll()
    business_ids = set([r['business_id'] for r in result])
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
    detail_id_list = q.queryByCustom('Select id From std_examination_info Where businessid In (Select businessid From std_examination_info Group By businessid Having Count(*)>1) and remark = "出科设置无需报名，自动进行报名" and create_time > "2023-06-20 14:59:00"')
    with open("del_sql.txt", "w") as f:
        for detail in detail_list:
            id = detail['id']
            plan_end_time = detail['plan_end_time']
            year = plan_end_time.year
            month = plan_end_time.month
            # print(id, plan_end_time, year, month)
            delete_sql = "DELETE FROM turn_plan_evaluation WHERE business_id = {} AND (year != {} OR (year = {} AND month != {}));\n".format(id, year, year, month)
            f.write(delete_sql)
        f.write("DELETE FROM turn_plan_evaluation WHERE business_id NOT IN (SELECT id FROM turn_plan_detail)")
