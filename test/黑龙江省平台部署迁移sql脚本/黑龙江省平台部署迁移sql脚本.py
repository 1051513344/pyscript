import csv
import uuid

with open('黑龙江省平台动态首页.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)[2:]

print(result)
sql = ""
for r in result:
    id = str(uuid.uuid4())
    unionId = "230108"
    hospitalId = r[3]
    type = "172"
    value = r[2]
    sql = sql + "insert into hospital_config(id, union_id, hospital_id, `type`, `value`) values ('{}','{}','{}','{}','{}')".format(
        id, unionId, hospitalId, type, value
    )
    sql = sql + ";\n"
with open("hospital_config_insert.sql", "w") as f:
    f.write(sql)



