from excel.exportExcel import exportExcel
from sql.query.queryDataFunc import QueryDB

if __name__ == "__main__":

    host = "sh-cdb-7hgrxn00.sql.tencentcdb.com"
    port = 63084
    user = "cccf_wxapp_czd"
    password = "AFeZk7BMcLMYmpDe"
    db = "cccf_prod"
    charset = "utf8mb4"
    table_name = "t_iw_doctor"

    # 获取需要导出的数据
    q = QueryDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )
    doctorList = q.queryAll()
    # 获取所有字段名
    q2 = QueryDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )
    columns = tuple(q2.queryTableMetaData())

    excelList = []
    for doctor in doctorList:
        l = []
        for column in columns:
            l.append(doctor[column])
        excelList.append(tuple(l))

    exportExcel("cccf医生数据", columns, excelList)
