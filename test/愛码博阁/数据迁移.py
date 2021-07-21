
from sql.query.queryDataFunc import *
from sql.insert.insertDataFunc import *
q = QueryDB(
    "185.216.116.188",
    3306,
    "root",
    "xsj26875676",
    "ssm_blog",
    "utf8mb4",
    "blog"
)
i = InsertDB(
    "49.235.243.221",
    3306,
    "root",
    "xsj26875676",
    "ssm_blog",
    "utf8mb4",
    "blog"
)


i.batchInsert(q.queryAll("344", "1"))





