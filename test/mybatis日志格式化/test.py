

mybatis_log = """

EXEC [dbo].[P_EcsOne_getServiceOrderList] @source = 'SEC', @comapnyCode = ?, @staffCode = ?, @tranStatus = ?, @tranType = ?, @tranCode = ?, @assetCode = ?, @outletNo = ?, @outletName = ?, @operationFlag = ?, @plantCode = ?, @maintenanceCodeList = ?, @startDate = ?, @endDate = ?, @pageIndex = ?, @pageSize = ?, @platform = ?, @techonlogyType = ?, @status = ?, @message = ?  

"""

params = "3039(String), JXSFS001(String), 1(Integer), (String), (String), (String), 1111111111(String), (String), 0(String), (String), JXSFS001(String), 2023-03-01(String), 2023-03-31(String), 1(Integer), 50(Integer), 1(Integer), (String)"

sql_segement = mybatis_log.split("?")
print(len(sql_segement))
params = params.split(", ")
print(len(params))
sql = ""
for s,param in zip(sql_segement,params):

    print(s)

    if "(String)" in param:
        param = param.replace("(String)", "")
        param = "'" + param + "'"
    else:
        param = param.replace("(Integer)", "")

    print(param)
    print("==========")
    # if param != "\"\"":
        # sql = sql + s + param
    # sql = sql + s + param
    if param == "\"\"":
        sql = sql + s + "\"0\""
    else:
        sql = sql + s + param
print(sql+", @status = '0', @message = '成功'")
