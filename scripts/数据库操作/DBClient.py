
"""
【解决方案】cx_Oracle.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle Client library
本贴最后更新于 699 天前，其中的信息可能已经沧海桑田
可能原因：

python版本和Oracle客户端instanceclient版本不对应；
缺少对应客户端instanceclient。
解决方案：

确认本地是否有可用的instanceclient，没有继续步骤2，有的话跳转步骤3
下载instanceclient（下载地址：https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html#license-lightbox）


【下载完毕后将客户端指向本地对应版本的客户端】
oracledb.init_oracle_client(lib_dir=r"D:\oracleclient\instantclient_21_14")
"""
import oracledb

class OracleClient:
    def __init__(self, username, password, host, port, server):
        dsn = f'{host}:{port}/{server}'
        oracledb.init_oracle_client(lib_dir=r"D:\oracleclient\instantclient_21_14")
        self.connection = oracledb.connect(user=username, password=password, dsn=dsn)
        self.cursor = self.connection.cursor()
    def selectOne(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result
    def selectList(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    def close(self):
        self.connection.close()

import pymysql.cursors

"""
    查询数据库
    queryAll  查询所有
    queryById 根据id查询
    queryByCondition  根据条件查询
    queryTableMetaData 查询表的所有字段
    queryTableMetaDataDict 查询表的所有字段及解释
    queryByCustom 自定义sql查询
"""
class MysqlClient:

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
    def connect(self):
        if self.connection._closed:
            self.connection = pymysql.connect(
                host=self.connection.host,
                port=self.connection.port,
                user=self.connection.user,
                password=self.connection.password,
                db=self.connection.db,
                charset=self.connection.charset,
                cursorclass=pymysql.cursors.DictCursor
            )

    def queryAll(self, start=None, end=None):
        """
        例 start=0 end=100 从0开始数100条
        """
        self.connect()
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
        self.connect()
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM {} WHERE id = %s ".format(self.table_name)
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
        finally:
            self.connection.close()
        return result

    def queryByCondition(self, limit_, _limit, orderBy, order, *args, **kwargs):
        self.connect()
        try:
            with self.connection.cursor() as cursor:
                if args is not None and args != ():
                    args = tuple([f"`{arg}`" for arg in args])
                    selectColumns = ",".join(args)
                    initSql = "SELECT {} FROM {} ".format(selectColumns, self.table_name)
                else:
                    initSql = "SELECT * FROM {} ".format(self.table_name)
                tempSql = ""
                if kwargs is not None and kwargs != {}:
                    initSql = initSql + " WHERE "
                    for key, value in zip(kwargs.keys(), kwargs.values()):
                        tempSql = tempSql + "`" + key + "`" + " = \"" + str(value) + "\" and "
                    tempSql = tempSql[:-4]
                if orderBy is not None:
                    tempSql = tempSql + f"order by {orderBy} "
                if order is not None:
                    tempSql = tempSql + order + " "
                if limit_ is not None and _limit is not None:
                    tempSql = tempSql + f"limit {limit_}, {_limit} "
                if limit_ is None and _limit is not None:
                    tempSql = tempSql + f"limit {_limit} "
                if limit_ is not None and _limit is None:
                    tempSql = tempSql + f"limit {limit_} "
                sql = initSql + tempSql
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
        return result

    def queryTableMetaData(self):
        self.connect()
        try:
            with self.connection.cursor() as cursor:
                sql = "select COLUMN_NAME from information_schema.COLUMNS  where table_name = '{}' and TABLE_SCHEMA='{}'".format(self.table_name, self.connection.db.decode())
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
        return [r.get('COLUMN_NAME') for r in result]

    def queryTableMetaDataDict(self, table_names):
        self.connect()
        tableNames = "("
        for table_name in table_names:
            tableNames = tableNames + "'" + table_name + "',"
        tableNames = tableNames[:-1] + ")"
        try:
            with self.connection.cursor() as cursor:
                sql = "select COLUMN_NAME, COLUMN_COMMENT from information_schema.COLUMNS  where table_name in {} and TABLE_SCHEMA = '{}'".format(tableNames, self.connection.db.decode())
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
        return result

    def queryByCustom(self, sql):
        self.connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            self.connection.close()
        return result
