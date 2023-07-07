
from excel.excelUtil import ExcelReader, ExcelExport

if __name__ == "__main__":

    token_project_name_dict = {}
    # 读取excel
    table = ExcelReader.read_excel("F:/workspace/~Python项目/pyscript/test\短信平台/token配置及使用情况统计", "Sheet1")
    rows = table.max_row  # 获取行数
    for i in range(1, rows):
        project_name = table.cell(row=i, column=1).value
        token = table.cell(row=i, column=2).value
        print(project_name, token)
        token_project_name_dict[token] = project_name

    columns_map = {
        "project_name": "项目名",
        "sms_token": "token",
        "sms_channel_name": "渠道",
        "January": "202301",
        "February": "202302",
        "March": "202303",
        "April": "202304",
        "May": "202305",
        "June": "202306",
    }
    excel_rows = []
    table = ExcelReader.read_excel("F:/文件/~短信平台/数据导出分析/按token查询短信发送量统计2023-01-01~2023-06-30", "Sheet1")
    rows = table.max_row  # 获取行数
    for i in range(3, rows):
        sms_token = table.cell(row=i, column=2).value
        sms_channel_name = table.cell(row=i, column=3).value
        January = table.cell(row=i, column=4).value
        February = table.cell(row=i, column=5).value
        March = table.cell(row=i, column=6).value
        April = table.cell(row=i, column=7).value
        May = table.cell(row=i, column=8).value
        June = table.cell(row=i, column=9).value
        # print(sms_token, sms_channel_name, January, February, March, April, May, June)
        if sms_token in token_project_name_dict:
            project_name = token_project_name_dict[sms_token]
        else:
            project_name = None
        excel_rows.append(
            {
                "project_name": project_name,
                "sms_token": sms_token,
                "sms_channel_name": sms_channel_name,
                "January": January,
                "February": February,
                "March": March,
                "April": April,
                "May": May,
                "June": June,
            }
        )

    ExcelExport.export_excel("按token查询短信发送量统计2023-01-01~2023-06-30", columns_map, excel_rows)