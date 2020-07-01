import csv
# 初始化列表

def exportExcel(title, list):
    """
    :param title: 表头 => ("标题1", "标题2", "标题3", "标题4", "标题5")
    :param list: 数据 => [("数据1", "数据2", "数据3", "数据4", "数据5")]
    :return:
    """
    data = []
    data.append(title)
    with open('test.csv', 'a', newline='') as f:
        for i in list:
            data.append(i)
            # 实例化csv写数据对象
            writer = csv.writer(f)
            writer.writerows(data)