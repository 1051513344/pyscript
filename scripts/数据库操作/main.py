

from DBClient import *

if __name__ == "__main__":

    # username = ""
    # password = ""
    # host = ""
    # port = 1521
    # service = ""
    # client = OracleClient(username, password, host, port, service)
    # sql = """SELECT * FROM (
    #       SELECT t.*
    #       FROM HLZK.MENU t
    #       WHERE NAME = '全院敏感指标追踪表'
    #   ) WHERE ROWNUM <= 101"""
    # result = client.selectList(sql)
    # client.close()
    # print(result)


    username = ""
    password = ""
    host = ""
    port = 3306
    db = ""
    charset = "utf8"
    table_name = ""
    client = MysqlClient(host, port, username, password, db, charset, table_name)
    result = client.queryAll(0, 1)
    print(result)

