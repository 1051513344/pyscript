

from OracleClient import OracleClient

if __name__ == "__main__":

    username = ""
    password = ""
    host = ""
    port = 1521
    service = "oraclepdb"
    client = OracleClient(username, password, host, port, service)
    sql = """SELECT * FROM (
          SELECT t.*
          FROM HLZK.MENU t
          WHERE NAME = '全院敏感指标追踪表'
      ) WHERE ROWNUM <= 101"""
    result = client.selectList(sql)
    client.close()
    print(result)

