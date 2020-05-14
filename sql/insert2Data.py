import pymysql.cursors
import random
# Connect to the database
connection = pymysql.connect(host='host',
                             user='root',
                             password='psswd',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def insert(conn):

    with conn.cursor() as cursor:
        # Create a new record
        cursor.execute("select COLUMN_NAME from information_schema.COLUMNS  where table_name = 'worker'")
        result = cursor.fetchall()
        columns = str(tuple([i["COLUMN_NAME"] for i in result])).replace("'", "")


        vx = "("

        for i in range(1, len(result)+1):
            vx = vx + "%s, "
        vx = vx[:-2]
        vx = vx + ")"

        for i in range(1, 5):

            sql = "INSERT INTO " \
                  "`worker` " \
                  "{} " \
                  "VALUES " \
                  "{}".format(columns, vx)

            cursor.execute(sql, (
                '{}'.format(i),
                '{}'.format(i*random.randint(1, 257)),
                '{}部'.format(random.choice(["工信", "科技", "人事", "实施"])),
                '{}{}'.format(random.choice(["张三", "李四", "王五", "赵六"]), random.randint(1, 2000)),
                '{}'.format(random.randint(20, 60)),
                '{}'.format(random.choice(["男", "女"]))
            ))

    conn.commit()

insert(connection)

connection.close()
