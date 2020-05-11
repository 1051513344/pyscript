import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='106.54.196.44',
                             user='root',
                             password='passwd',
                             db='web',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def insert(conn):

    with conn.cursor() as cursor:
        # Create a new record
        for i in range(1, 100):
            sql = "INSERT INTO " \
                  "`head` " \
                  "(`eye`, `nose`, `mouth`, `ears`, `human_id`) " \
                  "VALUES " \
                  "(%s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                '眼睛{}'.format(i),
                '鼻子{}'.format(i),
                '嘴巴{}'.format(i),
                '耳朵{}'.format(i),
                '{}'.format(i),
            ))

    conn.commit()

# insert(connection)

connection.close()
