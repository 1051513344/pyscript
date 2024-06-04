
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