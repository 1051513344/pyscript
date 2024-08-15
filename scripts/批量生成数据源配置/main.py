# -*- coding: gbk -*-
import uuid
import time

if __name__ == "__main__":

    mode_id = 25
    mode_name = "���ڻ������ϵͳoracle���ݿ�"
    mode_sql = f"INSERT INTO CT_CONNECTION_MODE (ID, CONNECTION_TYPE, CONNECTION_NAME, IS_DEFAULT, XML_CONTENT, IS_FORCED_TO_LOAD) VALUES ({mode_id}, 'db', '{mode_name}', 0, null, 0);"
    print(mode_sql, "\n")

    alias = "nurse"
    driverClassName = "oracle.jdbc.OracleDriver"
    url = "jdbc:oracle:thin:@192.168.151.114:1521/ewellpdb"
    # username = "root"
    # password = "xsj123456"
    username = "hlzk"
    password = "ewell123"
    detail_id = uuid.uuid1()
    details_sql = f"""
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'alias', '{alias}', '�����ݿ��������his,mcs,lis��(����)(�ƶ�������񿿱���ʶ���Ӧ����Դ����ʼ����������ò�Ҫ�޸�)', 1, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'driverClassName', '{driverClassName}', '���ݿ���������������', 2, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'url', '{url}', '�����ݿ��ַ����(����)', 3, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'username', '{username}', '�����ݿ��˺�(����)', 4, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'password', '{password}', '�����ݿ�����(����)', 5, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'filters', 'stat', '�� stat �� �������ͳ�ƣ��������������mcs��his����������������ã������ҳ��ַ��http://�ƶ���������ַ:�˿�/��Ŀ��/druid��', 6, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'validationQuery', null, '������������Ƿ���Ч��sql������oralce,mysql��select 1 from dual��sqlserve��select 1��', 7, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'testOnBorrow', null, '��������ʱ��������Ƿ���Ч��Ӱ������(�������������ã����ǹ�һ��ʱ��ͻ�����������崻��������������һ��)������true/false��', 8, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'testOnReturn', null, '�黹����ʱ��������Ƿ���Ч��Ӱ�����ܣ�����true/false��', 9, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'testWhileIdle', 'true', '�ｨ������Ϊtrue����Ч���������ӵ�ʱ���⣬�������ʱ�����timeBetweenEvictionRunsMillis����������Ƿ���Ч������true/false����', 10, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'timeBetweenEvictionRunsMillis', null, '���������ӵ�Ƶ�ʣ���λ����, ��������ʱ��ʾ�����м��', 11, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'poolPreparedStatements', 'true', '�Ƿ񻺴�preparedStatement��Ҳ����PSCache��PSCache��֧���α�����ݿ����������޴󣬱���˵oracle;(����true/false)', 12, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'maxPoolPreparedStatementPerConnectionSize', '100', 'Ҫ����PSCache���������ô���0��ÿ��������໺����ٸ�SQL', 13, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'initialSize', null, '��ʼ��ʱ�����������ӵĸ���', 14, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'maxActive', '50', '������ӳ�����,���ӳ������֧�ֶ��ٸ���Ự������', 15, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'maxWait', '30000', '��ȡ����ʱ���ȴ�ʱ�䣬��λ����', 16, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'minEvictableIdleTimeMillis', null, '����һ�������ڳ�����С�����ʱ�䣬��λ�Ǻ���', 17, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'removeAbandoned', null, '��ȡ���ӣ�N���ǿ�ƻ��գ����������ǻ�Ծ�Ļ��ǿ��е�(�������ɻ������ǲ������ģ���������δ�����رյ����ʱʹ��)������true/false��', 18, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'removeAbandonedTimeout', null, 'removeAbandoned������˵��N�룬��λ��(������Ӧ����ҵ�������ʱ��)', 19, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'logAbandoned', null, 'ǿ�ƻ������Ӻ󣬴�ӡ��־��������true/false��', 20, 0);
    """
    detail_sqls = details_sql.replace("   ", "").split("\n")
    detail_sqls = [sql for sql in detail_sqls if sql != "" and sql != "    "]
    for detail_sql in detail_sqls:
        time.sleep(0.1)
        print(detail_sql.replace(str(detail_id), str(uuid.uuid1())).replace(" INSERT ", "INSERT "))

    syn_id = 38
    syn_type = 'BlOOD_SUGAR'
    view = 'v_ydhl_xtsj'
    syn_name = 'Ѫ����ͼ'
    syn_sql = f"INSERT INTO CT_INFO_SYN_BASE_CONF (ID, SYN_TYPE, LOCAL_TABLE_NAME, INTERFACE_NAME, IS_USE_JOB, JOB_CLASS, JOB_CRON, JOB_PARAM, DATA_ACQUIRE_TYPE, CONNECTION_MODE_ID, INTERFACE_TYPE, SYN_TYPE_NAME, REMARK1) VALUES ({syn_id}, '{syn_type}', null, '{view}', 0, null, null, null, 0, {mode_id}, 'view', '{syn_name}', null);"
    print(syn_sql, "\n")

    data_init_list = [
        {"column": "patientId", "column_desc": "����ID", "column_type": "STRING"},
        {"column": "mrn", "column_desc": "סԺ��", "column_type": "STRING"},
        {"column": "series", "column_desc": "סԺ����", "column_type": "STRING"},
        {"column": "recordTime", "column_desc": "��¼ʱ��", "column_type": "STRING"},
        {"column": "recordType", "column_desc": "Ѫ������", "column_type": "STRING"},
        {"column": "recordValue", "column_desc": "��ֵmmol/L", "column_type": "STRING"},
        {"column": "userCode", "column_desc": "����", "column_type": "STRING"},
        {"column": "userName", "column_desc": "����", "column_type": "STRING"},
        {"column": "updateFlag", "column_desc": "״̬", "column_type": "STRING"}
    ]
    data_init_id = 380001
    data_init_seq = 1
    for data_init in data_init_list:
        column = data_init['column']
        column_desc = data_init['column_desc']
        column_type = data_init['column_type']
        data_init_sql = f"INSERT INTO CT_INFO_SYN_DATA_INIT (ID, SYN_TYPE, ENTITY_ATTRIBUTE, ENTITY_DESC, LOCAL_COLUMN, LOCAL_COLUMN_TYPE, SEQ, IS_IDENTITY_COLUMN, IS_NOT_NULL, ALLOWABLE_VALUES, IS_UNIQUE, SPECIAL_RULES) VALUES ({data_init_id}, '{syn_type}', '{column}', '{column_desc}', null, '{column_type}', {data_init_seq}, 0, 0, null, 0, null);"
        time.sleep(0.1)
        data_conf_sql = f"INSERT INTO CT_INFO_SYN_DATA_CONF (ID, INTERFACE_TYPE, INIT_DATA_ID, SYN_TYPE, ENTITY_ATTRIBUTE, ENTITY_DESC, LOCAL_COLUMN, LOCAL_COLUMN_TYPE, INTERFACE_COLUMN, INTERFACE_COLUMN_TYPE, INTERFACE_COLUMN_DATE_FORMAT, IS_DEFAULT, DEFAULT_VALUE, SEQ, SYN_METHOD, IS_FILTER_SPECIAL_CHARACTOR) VALUES ('{uuid.uuid1()}', 'view', {data_init_id}, '{syn_type}', '{column}', '{column_desc}', null, '{column_type}', null, null, null, 0, null, {data_init_seq}, 0, 0);"
        print(data_init_sql)
        print(data_conf_sql)

        data_init_id = data_init_id + 1
        data_init_seq = data_init_seq + 1



