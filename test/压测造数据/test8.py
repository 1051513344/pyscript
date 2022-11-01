
# 轮转进度查询页面改据加载

# 插入 turn_plan_detail 数据

from sql.insert.insertDataFunc import InsertDB

if __name__ == "__main__":

    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "password"
    db = "db"
    charset = "charset"
    table_name = "table_name"

    i = InsertDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )

    i.execute_custom(3, None)



