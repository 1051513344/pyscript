# -*- coding: gbk -*-
import uuid
import time

if __name__ == "__main__":

    mode_id = 25
    mode_name = "云在护理管理系统oracle数据库"
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
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'alias', '{alias}', '★数据库别名，如his,mcs,lis等(必填)(移动护理服务靠别名识别对应数据源，初始库给出的配置不要修改)', 1, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'driverClassName', '{driverClassName}', '数据库驱动程序类名称', 2, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'url', '{url}', '★数据库地址配置(必填)', 3, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'username', '{username}', '★数据库账号(必填)', 4, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'password', '{password}', '★数据库密码(必填)', 5, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'filters', 'stat', '填 stat ， 启动监控统计，不填不启动（建议mcs和his开启，其他看情况用，监控网页地址：http://移动护理服务地址:端口/项目名/druid）', 6, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'validationQuery', null, '用来检测连接是否有效的sql（比如oralce,mysql用select 1 from dual；sqlserve用select 1）', 7, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'testOnBorrow', null, '申请连接时检测连接是否有效，影响性能(如遇连接数够用，但是过一段时间就会连接数超额宕机的情况，开启试一下)（配置true/false）', 8, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'testOnReturn', null, '归还连接时检测连接是否有效，影响性能（配置true/false）', 9, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'testWhileIdle', 'true', '★建议配置为true，高效。申请连接的时候检测，如果空闲时间大于timeBetweenEvictionRunsMillis，检测连接是否有效（配置true/false））', 10, 1);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'timeBetweenEvictionRunsMillis', null, '检查空闲连接的频率，单位毫秒, 非正整数时表示不进行检查', 11, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'poolPreparedStatements', 'true', '是否缓存preparedStatement，也就是PSCache。PSCache对支持游标的数据库性能提升巨大，比如说oracle;(配置true/false)', 12, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'maxPoolPreparedStatementPerConnectionSize', '100', '要启用PSCache，必须配置大于0，每个连接最多缓存多少个SQL', 13, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'initialSize', null, '初始化时建立物理连接的个数', 14, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'maxActive', '50', '最大连接池数量,连接池中最多支持多少个活动会话的数量', 15, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'maxWait', '30000', '获取连接时最大等待时间，单位毫秒', 16, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'minEvictableIdleTimeMillis', null, '配置一个连接在池中最小生存的时间，单位是毫秒', 17, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'removeAbandoned', null, '获取连接，N秒后强制回收，不管连接是活跃的还是空闲的(正常生成环境中是不开启的，如遇连接未正常关闭的情况时使用)（配置true/false）', 18, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'removeAbandonedTimeout', null, 'removeAbandoned配置中说的N秒，单位秒(理论上应大于业务运行最长时间)', 19, 0);
    INSERT INTO CT_CONNECTION_DETAILS (ID, MODE_ID, CONF_TYPE, CONF_KEY, CONF_VALUE, CONF_DESC, SEQ, IS_REQUIRED_FIELDS) VALUES ('{detail_id}', {mode_id}, 'connection-db', 'logAbandoned', null, '强制回收连接后，打印日志。（配置true/false）', 20, 0);
    """
    detail_sqls = details_sql.replace("   ", "").split("\n")
    detail_sqls = [sql for sql in detail_sqls if sql != "" and sql != "    "]
    for detail_sql in detail_sqls:
        time.sleep(0.1)
        print(detail_sql.replace(str(detail_id), str(uuid.uuid1())).replace(" INSERT ", "INSERT "))

    syn_id = 38
    syn_type = 'BlOOD_SUGAR'
    view = 'v_ydhl_xtsj'
    syn_name = '血糖视图'
    syn_sql = f"INSERT INTO CT_INFO_SYN_BASE_CONF (ID, SYN_TYPE, LOCAL_TABLE_NAME, INTERFACE_NAME, IS_USE_JOB, JOB_CLASS, JOB_CRON, JOB_PARAM, DATA_ACQUIRE_TYPE, CONNECTION_MODE_ID, INTERFACE_TYPE, SYN_TYPE_NAME, REMARK1) VALUES ({syn_id}, '{syn_type}', null, '{view}', 0, null, null, null, 0, {mode_id}, 'view', '{syn_name}', null);"
    print(syn_sql, "\n")

    data_init_list = [
        {"column": "patientId", "column_desc": "病人ID", "column_type": "STRING"},
        {"column": "mrn", "column_desc": "住院号", "column_type": "STRING"},
        {"column": "series", "column_desc": "住院次数", "column_type": "STRING"},
        {"column": "recordTime", "column_desc": "记录时间", "column_type": "STRING"},
        {"column": "recordType", "column_desc": "血糖类型", "column_type": "STRING"},
        {"column": "recordValue", "column_desc": "数值mmol/L", "column_type": "STRING"},
        {"column": "userCode", "column_desc": "工号", "column_type": "STRING"},
        {"column": "userName", "column_desc": "姓名", "column_type": "STRING"},
        {"column": "updateFlag", "column_desc": "状态", "column_type": "STRING"}
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



