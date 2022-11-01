
# 教学管理课表管理页面数据加载

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

    i.execute_custom(7, None)

