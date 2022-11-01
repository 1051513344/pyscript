import pymysql.cursors
import random
import datetime
import radar

"""
    批量插入随机数据到数据库中
"""
class InsertDB:

    def __init__(self, host, port, user, password, db, charset, table_name):

        self.table_name = table_name
        self.connection = pymysql.connect(host=host,
                                     port=port,
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset=charset,
                                     cursorclass=pymysql.cursors.DictCursor)


    def insert(self, cursor, db_name, *args):

        # Create a new record
        cursor.execute("select COLUMN_NAME from information_schema.COLUMNS  where table_name = '{}' and TABLE_SCHEMA='{}'".format(self.table_name, db_name))
        result = cursor.fetchall()
        columns = str(tuple([i["COLUMN_NAME"] for i in result])).replace("'", "`")


        vx = "("

        for i in range(1, len(result)+1):
            vx = vx + "%s, "
        vx = vx[:-2]
        vx = vx + ")"

        sql = "INSERT INTO " \
              "`{}` " \
              "{} " \
              "VALUES " \
              "{}".format(self.table_name, columns, vx)

        cursor.execute(sql, args)

    def insert_custom(self, cursor, db_name, insert_columns, *args):

        # Create a new record
        cursor.execute("select COLUMN_NAME from information_schema.COLUMNS  where table_name = '{}' and TABLE_SCHEMA='{}' and COLUMN_NAME in {}".format(self.table_name, db_name, insert_columns))
        result = cursor.fetchall()
        columns = str(tuple([i["COLUMN_NAME"] for i in result])).replace("'", "`")


        vx = "("

        for i in range(1, len(result)+1):
            vx = vx + "%s, "
        vx = vx[:-2]
        vx = vx + ")"

        sql = "INSERT INTO " \
              "`{}` " \
              "{} " \
              "VALUES " \
              "{}".format(self.table_name, columns, vx)

        cursor.execute(sql, args)

    # 批量插入
    def batchInsert(self, list):
        with self.connection.cursor() as cursor:
            for i in list:
                id = i.get("id")
                title = i.get("title")
                content = i.get("content")
                read_times = i.get("read_times")
                comment_times = i.get("comment_times")
                type_id = i.get("type_id")
                blogger_id = i.get("blogger_id")
                create_time = i.get("create_time")
                update_time = i.get("update_time")
                zan = i.get("zan")
                hot = i.get("hot")
                type = i.get("type")
                is_delete = i.get("is_delete")
                self.insert(cursor, "ssm_blog",
                            id, title, content, read_times, comment_times, type_id,
                            blogger_id, create_time, update_time, zan, hot, type,
                            is_delete)

        self.connection.commit()
        self.connection.close()

    # 批量随机插入
    def execute(self, insert_num):
        with self.connection.cursor() as cursor:
            for i in range(1, insert_num + 1):
                print("正在插入 第{}条......".format(i))

                work_id = '{}'.format(i * random.randint(1000, 2577))
                name = '{}{}'.format(random.choice(["张三", "李四", "王五", "赵六"]), random.randint(1, 2000))
                age = '{}'.format(random.randint(20, 60))
                sex = '{}'.format(random.choice(["男", "女"]))
                department = '{}部'.format(random.choice(["工信", "科技", "人事", "实施"]))
                # phone = '1391106{}'.format(random.randint(1001, 9999))
                # id_card = '330327{}{}{}{}'.format(random.randint(1900, 2015), random.randint(1, 12), random.randint(1, 29),
                #                                   random.randint(1053, 9999))
                # email = '123456789@{}.com'.format(random.choice(["qq", "wx", "zxc", "xl"]))
                # # 时间戳
                # time = '158397{}'.format(random.randint(1000, 9999))
                # TODO 根据数据库表的列数插入对应的数据
                self.insert(cursor, "test", i, work_id, department, name, age, sex)

        self.connection.commit()
        self.connection.close()

    def execute_custom(self, test_No, datas):
        if test_No == 1:
            with self.connection.cursor() as cursor:
                id = 222
                leave_type = str(random.randint(0, 5))
                delta = datetime.timedelta(days=1)
                remark = "压测本科生请假一天"
                sys_type = "2"
                i = 1
                for data in datas:
                    uid = data["id"]
                    print("正在插入 第{}条 请假学生 {}......".format(i, data["name"]))
                    random_datetime = radar.random_datetime("2022-10-19T00:00:00", "2022-12-31T23:23:59")
                    start_date = random_datetime.strftime('%Y-%m-%d')
                    end_date = (random_datetime + delta).strftime('%Y-%m-%d')
                    self.insert(cursor, self.connection.db.decode(), id, uid, leave_type, start_date, end_date, remark, sys_type, None, None)
                    if int(data["name"].replace("压测本科生", "")) % 1000 == 0:
                        print("=============提交插入中...============")
                        self.connection.commit()
                        print("=============提交插入完毕...============")
                    i = i + 1
                    id = id + 1
        # =========================================================================================
        if test_No == 2:
            with self.connection.cursor() as cursor:
                id = 50719
                plan_id = None
                entrusted_unit = None
                prof_id = None
                type_id = None
                base_id = None
                dept_id = None
                master_discipline = None
                tutor = None
                hospital_tutor = None
                fresh = None
                practicing = None
                qualification_number = None
                isregister = None
                real_begin_time = None
                verification_years = None
                recruityear = None
                medical_unit = None
                hospital_attributes = None
                hospital_category = None
                hospital_nature = None
                hospital_level = None
                hospital_grade = None
                primary_medical = None
                cooperative = None
                cooperative_unit = None
                cooperative_nature = None
                coo_hospital_level = None
                coo_hospital_grade = None
                coo_hospital_category = None
                partner_assistance = None
                partner_assistance_unit = None
                first_assessment = None
                second_assessment = None
                third_assessment = None
                grad_theory_score = None
                grad_skill_score = None
                grad_direction = None
                status = 0
                graduation_year = None
                is_graduation = None
                turngrade = None
                educational = None
                degree = None
                degree_type = None
                create_at = datetime.datetime.now()
                update_at = None
                teacher_id = None
                for i in range(49001, 50001):
                    stu_id = 600000 + i
                    print("正在插入 第{}条 轮转学生id {}......".format(i, stu_id))
                    self.insert(cursor, self.connection.db.decode(), id, plan_id, stu_id,
                                entrusted_unit, prof_id, type_id,
                                base_id, dept_id, master_discipline,
                                tutor, hospital_tutor, fresh,
                                practicing, qualification_number, isregister,
                                real_begin_time, verification_years, recruityear,
                                medical_unit, hospital_attributes, hospital_category,
                                hospital_nature, hospital_level, hospital_grade,
                                primary_medical, cooperative, cooperative_unit,
                                cooperative_nature, coo_hospital_level, coo_hospital_grade,
                                coo_hospital_category, partner_assistance, partner_assistance_unit,
                                first_assessment, second_assessment, third_assessment,
                                grad_theory_score, grad_skill_score, grad_direction,
                                status, graduation_year, is_graduation,
                                turngrade, educational, degree,
                                degree_type, create_at, update_at,
                                teacher_id)
                    if stu_id % 1000 == 0:
                        print("=============提交插入中...============")
                        self.connection.commit()
                        print("=============提交插入完毕...============")
                    id = id + 1
        # =========================================================================================
        if test_No == 3:
            with self.connection.cursor() as cursor:
                id = 83150
                tec_id = None
                assign_tec_time = None
                num = 0
                real_begin_time = None
                real_end_time = None
                turn_status = 4
                status = 0
                turn_teaching_id = None
                remark = None
                turnchangeflag = None
                phase = None
                update_at = None
                update_by = None

                plan_begin_time_ = datetime.datetime.now()
                delta = datetime.timedelta(days=1)
                for i in range(1, 50001):
                    inter_id = 1718 + i
                    dept_id = 60000 + i
                    plan_begin_time = plan_begin_time_.strftime('%Y-%m-%d')
                    plan_end_time_ = plan_begin_time_ + delta
                    plan_end_time = plan_end_time_.strftime('%Y-%m-%d')
                    print("正在插入 第{}条 轮转计划关联id {}......".format(i, inter_id))
                    self.insert(cursor, self.connection.db.decode(), id, tec_id, assign_tec_time,
                                inter_id, num, dept_id,
                                plan_begin_time, plan_end_time, real_begin_time,
                                real_end_time, turn_status, status,
                                turn_teaching_id, remark, turnchangeflag,
                                phase, update_at, update_by)
                    if i % 1000 == 0:
                        print("=============提交插入中...============")
                        self.connection.commit()
                        print("=============提交插入完毕...============")
                    id = id + 1
                    plan_begin_time_ = plan_begin_time_ + delta
        # =========================================================================================
        if test_No == 4:
            with self.connection.cursor() as cursor:
                id = 10016
                insert_columns = ('id', 'uid', 'create_time')
                for i in range(1, 50001):
                    uid = 60000 + i
                    print("正在插入 第{}条 出科考试成绩 uid {}......".format(i, uid))
                    self.insert_custom(cursor, self.connection.db.decode(), insert_columns, id, uid, datetime.datetime.now())
                    if i % 1000 == 0:
                        print("=============提交插入中...============")
                        self.connection.commit()
                        print("=============提交插入完毕...============")
                    id = id + 1
        # =========================================================================================
        if test_No == 5:
            with self.connection.cursor() as cursor:
                id = 2332
                insert_columns = ('id', 'std_id', 'createtime')
                for i in range(1, 50001):
                    std_id = 60000 + i
                    print("正在插入 第{}条 住院医个人综合考评 std_id {}......".format(i, std_id))
                    self.insert_custom(cursor, self.connection.db.decode(), insert_columns, id, std_id, datetime.datetime.now())
                    if i % 1000 == 0:
                        print("=============提交插入中...============")
                        self.connection.commit()
                        print("=============提交插入完毕...============")
                    id = id + 1
        # =========================================================================================
        if test_No == 6:
            with self.connection.cursor() as cursor:
                id = 50222
                leave_type = str(random.randint(0, 5))
                delta = datetime.timedelta(days=1)
                remark = "压测住院医请假一天"
                sys_type = "1"
                i = 1
                for data in datas:
                    uid = data["id"]
                    print("正在插入 第{}条 请假学生 {}......".format(i, data["name"]))
                    random_datetime = radar.random_datetime("2022-10-19T00:00:00", "2022-12-31T23:23:59")
                    start_date = random_datetime.strftime('%Y-%m-%d')
                    end_date = (random_datetime + delta).strftime('%Y-%m-%d')
                    self.insert(cursor, self.connection.db.decode(), id, uid, leave_type, start_date, end_date, remark, sys_type, None, None)
                    if int(data["name"].replace("压测住院医", "")) % 1000 == 0:
                        print("=============提交插入中...============")
                        self.connection.commit()
                        print("=============提交插入完毕...============")
                    i = i + 1
                    id = id + 1
        # =========================================================================================
        if test_No == 7:
            with self.connection.cursor() as cursor:
                id = 4693
                insert_columns = ('id', 'start_dt', 'start_time', 'end_time', 'teacher_id')
                for i in range(1, 50001):
                    start_dt = datetime.datetime.now().timestamp()
                    start_time = datetime.datetime.now().timestamp()
                    end_time = datetime.datetime.now().timestamp()
                    teacher_id = -1
                    print("正在插入 第{}条 教学管理课表......".format(i))
                    self.insert_custom(cursor, self.connection.db.decode(), insert_columns, id, start_dt,
                                       start_time, end_time, teacher_id)
                    if i % 1000 == 0:
                        print("=============提交插入中...============")
                        self.connection.commit()
                        print("=============提交插入完毕...============")
                    id = id + 1


        self.connection.close()

if __name__ == "__main__":

    pass




