

from DBClient import *

if __name__ == "__main__":

    # username = "hlzk"
    # password = "HLZK123!"
    # host = "115.236.88.123"
    # port = 9200
    # service = "ewell"
    # client = OracleClient(username, password, host, port, service)
    # sql = """SELECT * FROM (
    #       SELECT t.*
    #       FROM HLZK.MENU t
    #       WHERE NAME = '全院敏感指标追踪表'
    #   ) WHERE ROWNUM <= 101"""
    # result = client.selectList(sql)
    # client.close()
    # print(result)


    username = "root"
    password = "xsj123456"
    host = "localhost"
    port = 32306
    db = "jeecg-boot"
    charset = "utf8"
    table_name = ""
    client = MysqlClient(host, port, username, password, db, charset, table_name)
    result = client.queryByCustom("SELECT concat('alter table ', TABLE_NAME, ' rename to ', lower(TABLE_NAME),';') FROM information_schema.TABLES WHERE TABLE_SCHEMA='jeecg-boot';")
    # print(result)
    for i in result:
        for k,v in i.items():
            print(v)
