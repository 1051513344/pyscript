

from DBClient import *

if __name__ == "__main__":

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

