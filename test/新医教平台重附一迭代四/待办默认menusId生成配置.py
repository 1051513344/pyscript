# -*- coding: utf-8 -*-



task_types = "1、个人预约 2、班级预约 3、出科考试预约 5、评教 6、行政课 7、问卷调查 8、课前作业 9、随堂小测 12、调课审批 14、评教住院医 15、评教带教 16、评教科室 17、护士长评教住院医 18、出科报名审核 19、教学活动上传图片 20、教学活动反馈 21、实习生评价带教老师 22、带教评价实习生-出科考核 23、带教评价实习生-DOPS 24、带教评价实习生-Mini-CEX 25、其它预约 26、班级预约审批和分配（宣武） 27、出科考核考官评分 28、出科鉴定 29、实习生出科考核 30、入科 31、出科 32、分配带教 33、轮转手册审核 34、大病历审核"

if __name__ == "__main__":

    for task_type in task_types.split(" "):
        task_type_value_name_split = task_type.split("、")
        task_type_value = task_type_value_name_split[0]
        task_type_name = task_type_value_name_split[1]
        # print(task_type_value, task_type_name)
        print(f"INSERT INTO `ucmed2-base`.`ck_commpara` (`param_code`, `param_name`, `param_value`, `param_1`, `param_2`, `param_3`, `param_4`, `param_5`, `param_6`, `param_7`, `param_8`, `param_9`, `param_10`, `param_11`, `param_12`, `param_13`, `param_14`, `param_15`, `param_16`, `param_17`, `param_18`, `param_19`, `param_20`, `start_time`, `end_time`, `created_at`, `updated_at`, `param_type`) VALUES ('appHomePageMenusId', '公众号首页待办菜单id配置，param_value为待办的类型task_type，param1为【{task_type_name}】菜单id', '{task_type_value}', '{task_type_value}', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2023-07-05 16:16:00', NULL, 1);")

