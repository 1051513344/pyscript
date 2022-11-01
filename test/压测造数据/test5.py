
# 考勤管理的全部页面数据数据加载

from sql.query.queryDataFunc import QueryDB
from sql.insert.insertDataFunc import InsertDB
import datetime

if __name__ == "__main__":

    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "password"
    db = "db"
    charset = "charset"
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

    压测本科生id_names = q.queryByCustom("select id,name from Users where name like '压测本科生%'")

    i = InsertDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )

    i.execute_custom(1, 压测本科生id_names)

