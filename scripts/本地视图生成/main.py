




if __name__ == "__main__":

    # 本地虚拟视图生成器

    sourse = """insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0160723029785', 'P0065V00', null, '悬浮红细胞（去白）', 2.00, 'U', 'AB', 'ZY040000247590', '0000247590', '4', '唐克意', '女', '85岁', '301738', '2001', to_date('15-09-2023 16:01:06', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-08-2023 13:38:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-10-2023 13:38:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-09-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'AB', '1', '0160723029785');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123082907', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'A', 'ZY010000259426', '0000259426', '1', '王淑芝', '女', '72岁', '302603', '2023', to_date('09-10-2023 09:44:02', 'dd-mm-yyyy hh24:mi:ss'), to_date('19-09-2023 11:48:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('24-10-2023 11:48:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('08-10-2023 08:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'A', '1', '0030123082907');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123078223', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'B', 'ZY010000258932', '0000258932', '1', '王玲', '女', '78岁', '301207', '2008', to_date('26-10-2023 15:02:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('12-10-2023 15:23:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('16-11-2023 15:23:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('26-10-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123078223');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0160723021863', 'P0065V00', null, '悬浮红细胞（去白）', 2.00, 'U', 'A', 'ZY010000261163', '0000261163', '1', '王秀敏', '女', '78岁', '301456', '2014', to_date('27-10-2023 09:57:26', 'dd-mm-yyyy hh24:mi:ss'), to_date('05-10-2023 09:57:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 09:57:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('27-10-2023 09:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'A', '1', '0160723021863');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123093494', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'B', 'ZY020000260723', '0000260723', '2', '吕丰浩', '男', '70岁', '301515', '2022', to_date('02-11-2023 12:09:17', 'dd-mm-yyyy hh24:mi:ss'), to_date('22-10-2023 14:03:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('26-11-2023 14:03:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('02-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123093494');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123086908', 'P0056V00', null, '悬浮红细胞', 1.00, 'U', 'B', 'ZY020000260723', '0000260723', '2', '吕丰浩', '男', '70岁', '301515', '2022', to_date('02-11-2023 17:10:44', 'dd-mm-yyyy hh24:mi:ss'), to_date('20-10-2023 15:38:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('24-11-2023 15:38:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123086908');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123086879', 'P0056V00', null, '悬浮红细胞', 1.00, 'U', 'B', 'ZY020000260723', '0000260723', '2', '吕丰浩', '男', '70岁', '301515', '2022', to_date('02-11-2023 17:10:44', 'dd-mm-yyyy hh24:mi:ss'), to_date('20-10-2023 13:36:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('24-11-2023 13:36:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123086879');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123099409', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'AB', 'ZY010000262191', '0000262191', '1', '庞继水', '男', '69岁', '301931', '2021', to_date('11-11-2023 01:42:05', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-10-2023 16:16:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-12-2023 16:16:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-11-2023 01:04:17', 'dd-mm-yyyy hh24:mi:ss'), null, 'AB', '1', '0030123099409');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123094974', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'AB', 'ZY040000247590', '0000247590', '4', '唐克意', '女', '85岁', '301738', '2001', to_date('13-11-2023 16:54:17', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-10-2023 13:22:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('05-12-2023 13:22:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'AB', '1', '0030123094974');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123082033', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'O', 'ZY010000262447', '0000262447', '1', '黄晶蕙', '女', '83岁', '301918', '2021', to_date('14-11-2023 10:31:22', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-10-2023 11:42:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('21-11-2023 11:42:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('13-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123082033');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123841330', 'P0142VB0', null, '去白细胞单采血小板', 1.00, '治疗量', 'O', 'ZY120000240306', '0000240306', '2', '樊少会', '女', '60岁', '301509', '2022', to_date('14-11-2023 10:44:37', 'dd-mm-yyyy hh24:mi:ss'), to_date('12-11-2023 11:11:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-11-2023 11:11:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('13-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123841330');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123091913', 'P0065V00', null, '悬浮红细胞（去白）', 2.00, 'U', 'B', 'ZY010000262280', '0000262280', '1', '付玉兰', '女', '77岁', '301932', '2021', to_date('14-11-2023 15:42:38', 'dd-mm-yyyy hh24:mi:ss'), to_date('02-11-2023 09:24:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('07-12-2023 09:24:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('10-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123091913');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123097067', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'A', 'ZY010000262298', '0000262298', '1', '赵广忠', '男', '81岁', '301938', '2021', to_date('14-11-2023 15:42:56', 'dd-mm-yyyy hh24:mi:ss'), to_date('21-10-2023 13:17:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('25-11-2023 13:17:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('10-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'A', '1', '0030123097067');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123066332', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'O', 'ZY120000240306', '0000240306', '2', '樊少会', '女', '60岁', '301509', '2022', to_date('14-11-2023 16:04:11', 'dd-mm-yyyy hh24:mi:ss'), to_date('18-10-2023 12:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('22-11-2023 12:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123066332');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123099213', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'A', 'ZY010000262145', '0000262145', '1', '刘淑玉', '女', '77岁', '301536', '2022', to_date('15-11-2023 15:57:13', 'dd-mm-yyyy hh24:mi:ss'), to_date('25-10-2023 14:04:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-11-2023 14:04:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('15-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'A', '1', '0030123099213');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123090944', 'P0056V00', null, '悬浮红细胞', 1.00, 'U', 'B', 'ZY010000262216', '0000262216', '1', '刘春林', '女', '73岁', '3019JC', '2021', to_date('16-11-2023 10:52:26', 'dd-mm-yyyy hh24:mi:ss'), to_date('01-11-2023 15:31:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('06-12-2023 15:31:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('15-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123090944');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123098098', 'P0056V00', null, '悬浮红细胞', 1.00, 'U', 'B', 'ZY010000262216', '0000262216', '1', '刘春林', '女', '73岁', '3019JC', '2021', to_date('16-11-2023 10:52:26', 'dd-mm-yyyy hh24:mi:ss'), to_date('01-11-2023 13:34:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('06-12-2023 13:34:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('15-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123098098');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123071012', 'P0065V00', null, '悬浮红细胞（去白）', 2.00, 'U', 'O', 'ZY020000254641', '0000254641', '2', '刘福卿', '男', '87岁', '301201', '2008', to_date('13-10-2023 11:36:46', 'dd-mm-yyyy hh24:mi:ss'), to_date('21-09-2023 14:55:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('26-10-2023 14:55:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-10-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123071012');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123081144', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'O', 'ZY020000254641', '0000254641', '2', '刘福卿', '男', '87岁', '301201', '2008', to_date('14-10-2023 11:42:27', 'dd-mm-yyyy hh24:mi:ss'), to_date('23-09-2023 10:21:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('28-10-2023 10:21:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-10-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123081144');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123085393', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY020000254641', '0000254641', '2', '刘福卿', '男', '87岁', '301201', '2008', to_date('14-10-2023 11:42:27', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-09-2023 10:14:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-09-2024 10:14:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-10-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123085393');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123085405', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY020000254641', '0000254641', '2', '刘福卿', '男', '87岁', '301201', '2008', to_date('14-10-2023 11:42:27', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-09-2023 10:58:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-09-2024 10:58:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-10-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123085405');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123098534', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'B', 'ZY030000248492', '0000248492', '3', '韩文章', '男', '53岁', '301212', '2008', to_date('11-11-2023 13:47:41', 'dd-mm-yyyy hh24:mi:ss'), to_date('26-10-2023 13:38:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('30-11-2023 13:38:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123098534');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123840931', 'P0142VB0', null, '去白细胞单采血小板', 1.00, '治疗量', 'O', 'ZY120000240306', '0000240306', '2', '樊少会', '女', '60岁', '301509', '2022', to_date('11-11-2023 16:05:03', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 11:34:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-11-2023 11:34:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123840931');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123840916', 'P0142VA0', null, '去白细胞单采血小板', 1.00, '治疗量', 'O', 'ZY010000261589', '0000261589', '1', '韩树龙', '男', '71岁', '301809', '2007', to_date('11-11-2023 16:45:50', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 10:40:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-11-2023 10:40:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-11-2023 16:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123840916');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123082426', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'B', 'ZY010000262407', '0000262407', '1', '刘桂英', '女', '78岁', '301919', '2021', to_date('12-11-2023 15:48:37', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-10-2023 12:58:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-12-2023 12:58:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('12-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'B', '1', '0030123082426');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123088575', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'AB', 'ZY030000246943', '0000246943', '3', '王素桂', '女', '78岁', '301504', '2022', to_date('08-11-2023 14:55:20', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-10-2023 15:08:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('18-11-2023 15:08:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('04-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'AB', '1', '0030123088575');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('371502305438655', 'D6611000', null, '悬浮红细胞（去白）', 2.00, 'U', 'AB', 'ZY010000262191', '0000262191', '1', '庞继水', '男', '69岁', '301931', '2021', to_date('08-11-2023 15:18:25', 'dd-mm-yyyy hh24:mi:ss'), to_date('14-10-2023 16:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('18-11-2023 16:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('08-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'AB', '1', '371502305438655');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123840541', 'P0142VA0', null, '去白细胞单采血小板', 1.00, '治疗量', 'O', 'ZY120000240306', '0000240306', '2', '樊少会', '女', '60岁', '3015JJ', '2022', to_date('08-11-2023 16:16:40', 'dd-mm-yyyy hh24:mi:ss'), to_date('06-11-2023 12:31:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-11-2023 12:31:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('08-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123840541');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123097899', 'P0056V00', null, '悬浮红细胞', 1.00, 'U', 'A', 'ZY010000262059', '0000262059', '1', '孙玉香', '女', '66岁', '302738', '2019', to_date('09-11-2023 14:25:37', 'dd-mm-yyyy hh24:mi:ss'), to_date('19-10-2023 15:44:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('23-11-2023 15:44:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('10-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'A', '1', '0030123097899');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123097890', 'P0056V00', null, '悬浮红细胞', 1.00, 'U', 'A', 'ZY010000262059', '0000262059', '1', '孙玉香', '女', '66岁', '302738', '2019', to_date('09-11-2023 14:25:37', 'dd-mm-yyyy hh24:mi:ss'), to_date('19-10-2023 14:44:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('23-11-2023 14:44:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('10-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'A', '1', '0030123097890');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123068189', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('22-08-2023 10:35:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('22-08-2024 10:35:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123068189');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123085846', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-10-2023 12:50:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-10-2024 12:50:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123085846');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123061731', 'P0151V00', null, '冰冻血浆', 150.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-08-2023 15:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-08-2024 15:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123061731');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123098116', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('02-11-2023 10:15:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('02-11-2024 10:15:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123098116');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123057384', 'P0151V00', null, '冰冻血浆', 150.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-08-2023 15:02:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-08-2024 15:02:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123057384');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123057303', 'P0151V00', null, '冰冻血浆', 150.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('01-08-2023 13:37:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('01-08-2024 13:37:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123057303');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123098115', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('02-11-2023 10:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('02-11-2024 10:10:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123098115');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123092496', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('13-10-2023 14:36:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('13-10-2024 14:36:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123092496');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123084487', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-10-2023 14:51:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-10-2024 14:51:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123084487');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123081825', 'P0147V00', null, '新鲜冰冻血浆', 200.00, 'ml', 'O', 'ZY040000238138', '0000238138', '4', '宋三居', '男', '80岁', '3012A2', '2008', to_date('10-11-2023 10:16:49', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-10-2023 10:18:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('11-10-2024 10:18:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123081825');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123840729', 'P0142VA0', null, '去白细胞单采血小板', 1.00, '治疗量', 'O', 'ZY120000240306', '0000240306', '2', '樊少会', '女', '60岁', '301509', '2022', to_date('10-11-2023 10:42:37', 'dd-mm-yyyy hh24:mi:ss'), to_date('07-11-2023 15:41:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('12-11-2023 15:41:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123840729');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123840729', 'P0142VB0', null, '去白细胞单采血小板', 1.00, '治疗量', 'O', 'ZY010000261589', '0000261589', '1', '韩树龙', '男', '71岁', '301809', '2007', to_date('10-11-2023 15:33:27', 'dd-mm-yyyy hh24:mi:ss'), to_date('07-11-2023 15:41:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('12-11-2023 15:41:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('10-11-2023 10:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'O', '1', '0030123840729');

insert into v_ewell_blood (PACK_NO, BAR_CODE, ORDER_NO, BLOOD_NAME, DOSAGE, UNIT, PACK_BLOOD_TYPE, PATIENT_ID, MRN, SERIES, PATIENT_NAME, SEX, AGE, BED_NO, WARD_CODE, GRANT_TIME, MAKE_TIME, EFFECTIVE_TIME, PLAN_TIME, SUIT_SYMPTOM, PATIENT_BLOOD_TYPE, RH_TYPE, APPLY_NO)
values ('0030123083972', 'P0056V00', null, '悬浮红细胞', 2.00, 'U', 'AB', 'ZY010000262191', '0000262191', '1', '庞继水', '男', '69岁', '301931', '2021', to_date('10-11-2023 16:01:50', 'dd-mm-yyyy hh24:mi:ss'), to_date('29-10-2023 12:27:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-12-2023 12:27:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('09-11-2023 15:00:00', 'dd-mm-yyyy hh24:mi:ss'), null, 'AB', '1', '0030123083972');"""

    virtualViewName = "v_ewell_blood"
    createViewSql = "create view {} as {}"
    for row in sourse.split("\n"):
        if row.startswith("insert into "):
            column = row.replace("insert into v_ewell_blood (", "").replace(")","").strip()
            break
    # print(column)
    columns = column.split(",")
    columnSql = ""
    for row in sourse.split("\n"):
        if row.startswith("values "):
            columnSql = columnSql + "select "
            value = row.replace("values (", "").strip()
            values = []
            tempValue = ""
            for v in value:
                if tempValue.startswith(" to_date"):
                    tempValue = tempValue + v
                    if tempValue.endswith(")"):
                        # print(tempValue)
                        values.append(tempValue)
                        tempValue = ""
                else:
                    if v == ",":
                        if tempValue != "":
                            # print(tempValue)
                            values.append(tempValue)
                        tempValue = ""
                    else:
                        tempValue = tempValue + v
                        if tempValue.endswith(");"):
                            tempValue = tempValue.replace(");", "")
                            values.append(tempValue)

            for c,v in zip(columns, values):
                columnSql = columnSql + f" {v} {c},"
            columnSql = columnSql[:-1] + " from dual\nunion all\n"
            # print(columnSql)
    # print(columnSql)
    createViewSql = createViewSql.format(virtualViewName, columnSql)
    print(createViewSql)






