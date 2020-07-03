import csv
# 初始化列表

def exportExcel(fileName, thead, list):
    """
    :param fileName: 文件名
    :param thead: 表头 => ("标题1", "标题2", "标题3", "标题4", "标题5")
    :param list: 数据 => [("数据1", "数据2", "数据3", "数据4", "数据5")]
    :return:
    """
    data = []
    data.append(thead)
    with open('{}.csv'.format(fileName), 'a', newline='') as f:
        for i in list:
            data.append(i)
        # 实例化csv写数据对象
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    fileName = "test"
    thead = ("标题1", "标题2", "标题3", "标题4", "标题5")
    list = [
        ("数据1", "数据2", "数据3", "数据4", "数据5"),
        ("数据1", "数据2", "数据3", "数据4", "数据5"),
        ("数据1", "数据2", "数据3", "数据4", "数据5"),
        ("数据1", "数据2", "数据3", "数据4", "数据5")
            ]
    exportExcel(fileName, thead, list)


