

mybatis_log = """

EXEC [dbo].[P_EcsOne_exportMarketServiceOrder] @companyCode = ?, @moduleCode = ?, @staffCode = ?, @queryStaffCode = ?, @maintenanceCodeList = '', @plantCode = ?, @statusCode = ?, @tranType = ?, @tranCode = ?, @assetCode = ?, @outletNo = ?, @outletName = ?, @technologyType = ?, @startDate = ?, @endDate = ?, @pageIndex = ?, @pageSize = ?, @status = ?, @message = ?

"""

params = "3006(String), (String), (String), (String), 3006(String), 2(String), (String), (String), (String), (String), (String), (String), 2022-10-01(String), 2022-10-31(String), 1(Integer), 20000(Integer)"

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
