import pymysql.cursors
import random



class InsertDB:

    def __init__(self, table_name):

        self.table_name = table_name
        self.connection = pymysql.connect(host='106.54.196.44',
                                     user='root',
                                     password='xsj26875676',
                                     db='test',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)


    def insert(self, cursor, *args):

        # Create a new record
        cursor.execute("select COLUMN_NAME from information_schema.COLUMNS  where table_name = '{}'".format(self.table_name))
        result = cursor.fetchall()
        columns = str(tuple([i["COLUMN_NAME"] for i in result])).replace("'", "")


        vx = "("

        for i in range(1, len(result)+1):
            vx = vx + "%s, "
        vx = vx[:-2]
        vx = vx + ")"




        sql = "INSERT INTO " \
              "`worker` " \
              "{} " \
              "VALUES " \
              "{}".format(columns, vx)

        arg_list = []
        for arg in args:
            arg_list.append(arg)

        cursor.execute(sql, tuple(arg_list))

    def execute(self, insert_num):

        with self.connection.cursor() as cursor:
            for i in range(1, insert_num + 1):
                print("正在插入 第{}条......".format(i))

                work_id = '{}'.format(i * random.randint(1000, 2577))
                name = '{}{}'.format(random.choice(["张三", "李四", "王五", "赵六"]), random.randint(1, 2000))
                age = '{}'.format(random.randint(20, 60))
                sex = '{}'.format(random.choice(["男", "女"]))
                department = '{}部'.format(random.choice(["工信", "科技", "人事", "实施"]))
                # phone = '1391106{}'.format(random.randint(1001, 9999))
                # id_card = '330327{}{}{}{}'.format(random.randint(1900, 2015), random.randint(1, 12), random.randint(1, 29),
                #                                   random.randint(1053, 9999))
                # email = '123456789@{}.com'.format(random.choice(["qq", "wx", "zxc", "xl"]))
                # # 时间戳
                # time = '158397{}'.format(random.randint(1000, 9999))

                self.insert(cursor, i, work_id, department, name, age, sex)

        self.connection.commit()

        self.connection.close()


if __name__ == "__main__":

    table_name = "worker"
    i = InsertDB(table_name)
    i.execute(500)




