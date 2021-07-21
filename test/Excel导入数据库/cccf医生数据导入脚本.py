import csv
import datetime
import pymysql.cursors

with open('cccf医生数据.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)


# Connect to the database
connection = pymysql.connect(host='sh-cdb-7hgrxn00.sql.tencentcdb.com',
                             port=63084,
                             user='cccf_wxapp_czd',
                             password='AFeZk7BMcLMYmpDe',
                             db='cccf_prod',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    # Create a new record
    for row in result[1:]:
        print("正在导入第{}个数据".format(row[0]))
        # id = row[0]
        name = row[1]
        avatar = row[2]
        sex = row[3]
        cate = row[4]
        job = row[5]
        hospital = row[6]
        office = row[7]
        degree = row[8]
        school = row[9]
        content = row[10]
        province = row[11]
        city = row[12]
        district = row[13]
        address = row[14]
        mobile = row[15]
        email = row[16]
        wechat = row[17]
        postcode = row[18]
        consult_time = row[19]
        # is_ask = row[20]
        is_ask = None
        # ask_doctor_id = row[21]
        ask_doctor_id = None
        sort = row[22]
        is_delete = row[23]
        update_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print(row)
        sql = "INSERT INTO " \
              "`t_iw_doctor` " \
              "(`name`, `avatar`, `sex`, `cate`, `job`, " \
              "`hospital`, `office`, `degree`, `school`, `content`, " \
              "`province`, `city`, `district`, `address`, `mobile`, " \
              "`email`, `wechat`, `postcode`, `consult_time`, `is_ask`, " \
              "`ask_doctor_id`, `sort`, `is_delete`, `update_at`, `created_at`) " \
              "VALUES " \
              "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            name, avatar, sex, cate, job,
            hospital, office, degree, school, content,
            province, city, district, address, mobile,
            email, wechat, postcode, consult_time, is_ask,
            ask_doctor_id, sort, is_delete, update_at, created_at
        ))
    connection.commit()

connection.close()



