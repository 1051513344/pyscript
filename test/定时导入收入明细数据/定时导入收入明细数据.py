import requests
import calendar
import time

def main():
    for month in range(5, 8):
        # print(month)
        days = calendar.monthrange(2020, month)[1]
        # print(days)
        # print(list(range(1, days + 1)))
        for day in range(1, days + 1):
            if month == 5 and day <= 16:
                continue
            if day // 10 > 0:
                date = "2020-0{}-{}".format(month, day)
            else:
                date = "2020-0{}-0{}".format(month, day)
            startTime = date + " 00:00:00"
            endTime = date + " 23:59:59"
            print("正在导入：", date)
            print("导入时间：", time.strftime("%H:%M:%S", time.localtime()))
            url = "https://hlwyyapi-hlj.zwjk.com/admin/invoice/saveIncomeDetail"
            param = {
                "token": "30218df560b1d83f2d0c77b72ca5f2d041d",
                "startTime": startTime,
                "endTime": endTime,
            }
            response = requests.post(url, param)
            print(response.text)
            print(date + "导入完成")
            print("=====================================================")
            # time.sleep(60*5)
    print("《《《《程序停止》》》》")

if __name__ == '__main__':
    main()


