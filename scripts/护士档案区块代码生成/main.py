import time

if __name__ == "__main__":
    import uuid
    import datetime

    parentBlockId = "923C4D9F01E044CFBC1DF26939FD097D"
    parentBlockCode = "SCIENTIFIC_RESEARCH"

    new_id = str(uuid.uuid4()).replace("-", "").upper()
    block_name = "专家共识/指南/标准/规范"
    block_sort = 8
    block_code = "EXPERT_CONSENSUS"
    now = datetime.datetime.now()
    nowTime = now.strftime("%Y-%m-%d %H:%M:%S")
    newBlockSql = f"INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH, ATTACHMENT) VALUES ('{new_id}', '{parentBlockId}', '{block_name}', {block_sort}, 1, 1, 0, 0, null, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', '{block_code}', '{parentBlockCode}', null, null, null, null, null, null, null, 1, null, null, '{block_code}', null, null, '{block_name}', 0, 0, 0, 0, 0, 100, 2, 0, 1, 0, 1, null, null);"
    print(newBlockSql)
    for groupId in ('a9184b5cd4e14ea7ab1d64c863df293b', '7d1967f8635a48e6ba8c36edba3f006b', '9602b6a5cd0c4cd0b978af5bfcd143fe', '00f46dfc1a0144c88034c26b698ca07b'):
        newBlockNqa_id = str(uuid.uuid4()).replace("-", "").upper()
        newBlockNqaSql = f"INSERT INTO NURSE_CONFIG_NQA_BLOCK_MAP (ID, BLOCK_ID, NQA_GROUP_ID, SORT, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID) VALUES ('{newBlockNqa_id}', '{new_id}', '{groupId}', null, null, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110');"
        print(newBlockNqaSql)
        time.sleep(0.3)

    fieldConfigList = [
        {
            "code": "type",
            "displayCode": "typeStr",
            "name": "类型",
            "optionType": 1,
            "dictCode": "EXPERT_CONSENSUS_TYPE",
            "dictName": "类型",
            "dict": [('EXPERT_CONSENSUS_TYPE_1', '专家共识'), ('EXPERT_CONSENSUS_TYPE_2', '指南'), ('EXPERT_CONSENSUS_TYPE_3', '标准'), ('EXPERT_CONSENSUS_TYPE_4', '规范')],
            "sort": 1
        },
        {
            "code": "name",
            "displayCode": "name",
            "name": "名称",
            "optionType": 3,
            "sort": 2
        },
        {
            "code": "publishDate",
            "displayCode": "publishDate",
            "name": "发布时间",
            "optionType": 5,
            "sort": 3
        },
        {
            "code": "authorType",
            "displayCode": "authorTypeStr",
            "name": "作者类型",
            "optionType": 1,
            "dictCode": "EXPERT_CONSENSUS_AUTHOR_TYPE",
            "dictName": "作者类型",
            "dict": [('EXPERT_CONSENSUS_AUTHOR_TYPE_1', '主要撰稿人'), ('EXPERT_CONSENSUS_AUTHOR_TYPE_2', '执笔'), ('EEXPERT_CONSENSUS_AUTHOR_TYPE_3', '主要起草人'), ('EXPERT_CONSENSUS_AUTHOR_TYPE_4', '其他')],
            "sort": 4
        },
        {
            "code": "remark",
            "displayCode": "remark",
            "name": "其他描述",
            "optionType": 3,
            "sort": 5
        },
        {
            "code": "url",
            "displayCode": "url",
            "name": "附件",
            "optionType": 9,
            "sort": 6
        },
    ]

    for fieldConfig in fieldConfigList:
        code = fieldConfig['code'] if 'code' in fieldConfig else "null"
        displayCode = fieldConfig['displayCode'] if 'displayCode' in fieldConfig else "null"
        name = fieldConfig['name'] if 'name' in fieldConfig else "null"
        optionType = fieldConfig['optionType'] if 'optionType' in fieldConfig else "null"
        dictCode = fieldConfig['dictCode'] if 'dictCode' in fieldConfig else "null"
        dictName = fieldConfig['dictName'] if 'dictName' in fieldConfig else "null"
        dict = fieldConfig['dict'] if 'dict' in fieldConfig else []
        sort = fieldConfig['sort'] if 'sort' in fieldConfig else 0
        new_block_id = str(uuid.uuid4()).replace("-", "").upper()
        time.sleep(0.3)
        # 字典类型字段
        if optionType == 1:
            dict_new_id = str(uuid.uuid4()).replace("-", "").upper()
            print(f"INSERT INTO DATA_DICT (ID, DEPTH, PARENT_ID, SORT, NAME, CODE, REMARK, CHILD_NUM, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, WEIGHT, ROOT_CODE, OTHER_NAME, PINYIN, NUM_VAR1) VALUES ('{dict_new_id}', 2, null, 162, '{dictName}', '{dictCode}', null, {len(dict)}, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', 1, null, null, '', null);")
            time.sleep(0.3)
            dict_sort = 1
            for d in dict:
                dict_child_new_id = str(uuid.uuid4()).replace("-", "").upper()
                print(f"INSERT INTO DATA_DICT (ID, DEPTH, PARENT_ID, SORT, NAME, CODE, REMARK, CHILD_NUM, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, WEIGHT, ROOT_CODE, OTHER_NAME, PINYIN, NUM_VAR1) VALUES ('{dict_child_new_id}', 3, '{dict_new_id}', {dict_sort}, '{d[1]}', '{d[0]}', null, 0, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', 1, null, null, '', null);")
                dict_sort = dict_sort + 1
                time.sleep(0.3)
            print(f"INSERT INTO DATA_DICT_GROUP_MAP (GROUP_ID, DICT_ID, SORT) VALUES ('20d56809ef574f35a5dbfdc982796053', '{dict_new_id}', 79);")
            print(f"INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('{new_block_id}', '{new_id}', '{name}', {sort}, 1, 1, 1, 1, null, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', '{code}', '{block_code}', {optionType}, '{dictCode}', null, null, 1, '{dictName}', 1, 1, null, null, '{displayCode}', null, null, '{name}', 1, 1, 0, 1, 0, 100, 2, 6, 1, 1, 1, null);")
        elif optionType == 3:
            print(f"INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('{new_block_id}', '{new_id}', '{name}', {sort}, 1, 1, 1, 1, null, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', '{code}', '{block_code}', {optionType}, null, null, null, 1, null, 1, 1, null, null, '{displayCode}', null, null, '{name}', 1, 1, 0, 1, 0, 100, 2, 6, 1, 1, 1, null);")
        elif optionType == 5:
            print(f"INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('{new_block_id}', '{new_id}', '{name}', {sort}, 1, 1, 1, 1, null, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', '{code}', '{block_code}', {optionType}, null, null, null, 4, null, 1, 1, null, null, '{displayCode}', null, null, '{name}', 1, 1, 0, 1, 0, 100, 2, 6, 1, 1, 1, null);")
        elif optionType == 9:
            print(f"INSERT INTO NURSE_DOSSIER_CONFIG_BLOCK (ID, PARENT_ID, NAME, SORT, CLASS_VIEW, BLOCK_VIEW, LIST_VIEW, EDIT_VIEW, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID, CODE, PARENT_CODE, OPTION_TYPE, DICT_CODE, DEFAULT_VALUE, PROPERTY_LENGTH, DATA_TYPE, DICT_NAME, IS_REQUIRED, BLOCK_TYPE, DATE_OPTION_TYPE, URL, DISPLAY_CODE, SUFFIX, CHECK_CODE, PROJECT_NAME, IS_VIEW, IS_IMPORT, IS_IMPORT_REQUIRED, IS_EXPORT, IS_QUERY, PROPERTY_WIDTH, PROPERTY_ALIGNMENT, LIST_SORT, IS_CLASS_VIEW, IS_BLOCK_VIEW, FILTER_FLAG, WIDTH) VALUES ('{new_block_id}', '{new_id}', '{name}', {sort}, 1, 1, 1, 1, null, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', '{code}', '{block_code}', {optionType}, null, null, null, 1, null, 1, 1, null, null, '{displayCode}', null, null, '{name}', 1, 1, 0, 1, 0, 100, 2, 6, 1, 1, 1, null);")

        for groupId in ('a9184b5cd4e14ea7ab1d64c863df293b', '7d1967f8635a48e6ba8c36edba3f006b', '9602b6a5cd0c4cd0b978af5bfcd143fe', '00f46dfc1a0144c88034c26b698ca07b'):
            newBlockNqa_id = str(uuid.uuid4()).replace("-", "").upper()
            newBlockNqaSql = f"INSERT INTO NURSE_CONFIG_NQA_BLOCK_MAP (ID, BLOCK_ID, NQA_GROUP_ID, SORT, REMARK, VALID_FLAG, CREATE_TIME, CREATE_ID, UPDATE_TIME, UPDATE_ID) VALUES ('{newBlockNqa_id}', '{new_block_id}', '{groupId}', null, null, 1, TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110', TO_DATE('{nowTime}', 'YYYY-MM-DD HH24:MI:SS'), 'SINCE20211110');"
            print(newBlockNqaSql)
            time.sleep(0.3)
