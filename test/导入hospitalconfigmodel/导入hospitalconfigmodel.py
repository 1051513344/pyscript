import pymysql.cursors

"""
    批量插入随机数据到数据库中
    table_name = "worker"    # 表名
    i = InsertDB(table_name) # 实例化
    i.execute(500)           # 插入随机数据500条
"""
class InsertDB:

    def __init__(self, host, port, user, password, db, charset, table_name):

        self.table_name = table_name
        self.connection = pymysql.connect(host=host,
                                     port=port,
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset=charset,
                                     cursorclass=pymysql.cursors.DictCursor)


    def insert(self, *args):

        with self.connection.cursor() as cursor:
            # Create a new record
            cursor.execute("select COLUMN_NAME from information_schema.COLUMNS  where table_name = '{}' and TABLE_SCHEMA='{}'".format(self.table_name, self.connection.db.decode()))
            result = cursor.fetchall()
            columns = str(tuple([i["COLUMN_NAME"] for i in result])).replace("'", "")


            vx = "("

            for i in range(1, len(result)+1):
                vx = vx + "%s, "
            vx = vx[:-2]
            vx = vx + ")"

            sql = "INSERT INTO " \
                  "`{}` " \
                  "{} " \
                  "VALUES " \
                  "{}".format(self.table_name, columns, vx)

            cursor.execute(sql, args)

        self.connection.commit()
        self.connection.close()

    

if __name__ == "__main__":

    host, port, user, password, db, charset, table_name = "192.168.1.19", 3306, "root", "hlwyy@mysql", "hlwyy-3.4", "utf8mb4", "hospital_config_model"

    i = InsertDB(host, port, user, password, db, charset, table_name)
    

    id = "4039"
    type = "4"
    type_code = "10086"
    title = "医生超过几次超时未回复冻结咨询功能 0表示未开通 默认5"
    type_describe = "医生超过几次超时未回复冻结咨询功能 0表示未开通 默认5"
    required = "0"
    style_type = "switchNumInput"
    options = None
    create_time = None
    update_time = None
    is_delete = "0"

    i.insert(id,type,type_code,title,type_describe,required,style_type,options,create_time,update_time,is_delete)




