import pymysql.cursors

from sql.query.queryDataFunc import QueryDB

"""
    更新数据库
    updateById 根据id更新
"""
class UpdateDB:

    def __init__(self, table_name):
        self.table_name = table_name
        self.connection = pymysql.connect(host='106.54.196.44',
                                          user='root',
                                          password='xsj26875676',
                                          db='test',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
    def updateById(self, id, **kwargs):
        try:
            with self.connection.cursor() as cursor:
                initSql = "update {} set ".format(self.table_name)
                tempSql = ""
                for key, value in zip(kwargs.keys(), kwargs.values()):
                    tempSql = tempSql + "`" + key + "`" + "=" + str(value) + " , "
                tempSql = tempSql[:-2] + "WHERE id = %s"
                sql = initSql + tempSql
                cursor.execute(sql, (id, ))
                self.connection.commit()
        finally:
            self.connection.close()



if __name__ == "__main__":

    table_name = "message_template"
    id = "10"
    q1 = QueryDB(table_name)
    print("更新前")
    print(q1.queryById(id))

    u = UpdateDB(table_name)
    u.updateById(id, union_id=130123, hospital_id="1118011814561100810")
    q2 = QueryDB(table_name)
    print("更新后")
    print(q2.queryById(id))


