
from sql.query.queryDataFunc import *
from sql.insert.insertDataFunc import *
q = QueryDB(
    "host",
    3306,
    "user",
    "passwd",
    "db",
    "utf8mb4",
    "table"
)
i = InsertDB(
    "host",
    3306,
    "user",
    "passwd",
    "db",
    "utf8mb4",
    "table"
)


i.batchInsert(q.queryAll("301", "20"))





