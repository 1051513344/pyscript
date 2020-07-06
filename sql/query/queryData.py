import pymysql.cursors

"""
    查询数据库
    queryAll  查询所有
    queryById 根据id查询
    queryByCondition  根据条件查询
"""
class QueryDB:

    def __init__(self, table_name):
        self.table_name = table_name
        self.connection = pymysql.connect(host='host',
                                          user='root',
                                          password='psswd',
                                          db='test',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
    def queryAll(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM {}".format(self.table_name)
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
        return result

    def queryById(self, id):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM {} WHERE id = %s ".format(self.table_name)
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
        finally:
            self.connection.close()
        return result

    def queryByCondition(self, **kwargs):
        try:
            with self.connection.cursor() as cursor:
                initSql = "SELECT * FROM {} WHERE ".format(self.table_name)
                tempSql = ""
                for key, value in zip(kwargs.keys(), kwargs.values()):
                    tempSql = tempSql + "`" + key + "`" + "=" + str(value) + " and "
                tempSql = tempSql[:-4]
                sql = initSql + tempSql
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
        return result



if __name__ == "__main__":

    # 查询所有
    table_name = "message_template"
    q = QueryDB(table_name)
    print(q.queryAll())

    # 根据id查询
    table_name = "message_template"
    q2 = QueryDB(table_name)
    print(q2.queryById("10"))

    # 根据条件查询
    table_name = "message_template"
    q3 = QueryDB(table_name)
    print(q3.queryByCondition(hospital_id="1118011814561100810", union_id="130123"))


