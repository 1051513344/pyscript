
# 教学管理-进度表管理/填报页面跳转

import psycopg2

if __name__ == "__main__":

    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "password"
    db = "db"
    charset = "charset"
    table_name = "table_name"

    conn = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
    insert_columns = '("id")'
    with conn.cursor() as cursor:
        cursor.execute("select column_name from information_schema.COLUMNS  where table_name = 'schedule' and column_name in ('id')")
        result = cursor.fetchall()
        columns = insert_columns

        id = 5412
        for i in range(1, 50001):

            print("正在插入 第{}条 进度表管理......".format(i))
            args = [id]
            vx = "("

            for x in range(1, len(result) + 1):
                vx = vx + "%s, "
            vx = vx[:-2]
            vx = vx + ")"

            sql = "INSERT INTO " \
                  "{} " \
                  "{} " \
                  "VALUES " \
                  "{}".format(table_name, insert_columns, vx)

            cursor.execute(sql, args)
            if i % 1000 == 0:
                print("=============提交插入中...============")
                conn.commit()
                print("=============提交插入完毕...============")
            id = id + 1

    conn.close()

