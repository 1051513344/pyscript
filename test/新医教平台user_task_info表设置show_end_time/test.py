from sql.query.queryDataFunc import QueryDB
from sql.update.updateDataFunc import UpdateDB
import datetime

if __name__ == "__main__":

    host = "***.***.***.***"
    port = 3306
    user = "user"
    password = "password"
    db = "ucmed2"
    charset = "utf8mb4"
    table_name = "table_name"

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
    评价 = q.queryByCondition(task_type=17)
    评价_source_ids = [i["source_id"] for i in 评价]

    table_name = "table_name2"
    q = QueryDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )
    评价_turn_plan_detail_plan_end_times = q.queryByCustom("SELECT id, plan_end_time FROM turn_plan_detail WHERE id in ({})".format(str(评价_source_ids).replace("[", "").replace("]", "")))
    id_plan_end_time_dict = {}

    for turn_plan_detail_plan_end_time in 评价_turn_plan_detail_plan_end_times:
        id_plan_end_time_dict[turn_plan_detail_plan_end_time["id"]] = datetime.datetime.strptime(str(turn_plan_detail_plan_end_time["plan_end_time"]) + " 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp()

    table_name = "table_name"
    u = UpdateDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )
    for task in 评价:
        id = task["id"]
        timestamp = id_plan_end_time_dict.get(task["source_id"])
        if timestamp is not None:
            print("start {}".format(id))
            u.batchUpdate(id, id_plan_end_time_dict.get(task["source_id"]))
            print("end   {}".format(id))
    u.colse()