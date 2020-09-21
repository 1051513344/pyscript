import pymysql.cursors

"""
    查询数据库
    queryAll  查询所有
    queryById 根据id查询
    queryByCondition  根据条件查询
    queryTableMetaData 查询表的所有字段
"""
class QueryDB:

    def __init__(self, host, port, user, password, db, charset,
                 table_name):
        self.table_name = table_name
        self.connection = pymysql.connect(host=host,
                                          port=port,
                                          user=user,
                                          password=password,
                                          db=db,
                                          charset=charset,
                                          cursorclass=pymysql.cursors.DictCursor)
    def queryAll(self, start=None, end=None):
        """
        例 start=0 end=100 从0开始数100条
        """
        limit = ""
        if (start is not None) and (end is not None):
            limit = "limit {} offset {}".format(end, start)
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM {} {}".format(self.table_name, limit)
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

    def queryTableMetaData(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "select COLUMN_NAME from information_schema.COLUMNS  where table_name = '{}' and TABLE_SCHEMA='{}'".format(self.table_name, db)
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
        return [r.get('COLUMN_NAME') for r in result]



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


