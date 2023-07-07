import requests


class smsPlatXhr:

    def __init__(self, cookie):
        self.cookie = cookie

    # 总限
    def getLimit(self, token):
        response = requests.post(url='http://smsmanager.zwjk.com/admin/tokens.htm?action=getLimit', data={'token': token},
                      headers={'Cookie': self.cookie, 'Content-Type': 'application/x-www-form-urlencoded'})
        responseJson = response.json()
        response.close()
        return responseJson

    def getTotalMaxCount(self, token):
        responseJson = self.getLimit(token)
        if "model" in responseJson:
            return responseJson['model']['totalMaxCount']
        else:
            return ""

    # 限流
    def limit(self, token):
        response = requests.post(url='http://smsmanager.zwjk.com/admin/tokens.htm?action=limit',
                                 data={'token': token},
                                 headers={'Cookie': self.cookie, 'Content-Type': 'application/x-www-form-urlencoded'})
        responseJson = response.json()
        response.close()
        return responseJson

    def getLimitData(self, token):
        responseJson = self.limit(token)
        if "model" in responseJson:
            return responseJson['model']['interval'], responseJson['model']['maxCount']
        else:
            return None, None

    # 是否禁用
    def getDisabled(self, tokenid):
        response = requests.post(url='http://smsmanager.zwjk.com/admin/tokens.htm?action=getDisabled',
                                 data={'tokenid': tokenid},
                                 headers={'Cookie': self.cookie,
                                          'Content-Type': 'application/x-www-form-urlencoded'})
        responseJson = response.json()
        response.close()
        return responseJson

    def getDisabledValue(self, tokenid):
        responseJson = self.getDisabled(tokenid)
        if "model" in responseJson:
            return responseJson['model']['disabled']
        else:
            return None

if __name__ == "__main__":
    cookie = input("Cookie: ")
    smsPlatXhr = smsPlatXhr(cookie)
    # print(smsPlatXhr.getTotalMaxCount("rBu975euMPoNaiQ7G8W"))
    # interval, maxCount = smsPlatXhr.getLimitData("rBu975euMPoNaiQ7G8W")
    # print(interval, maxCount)
    print(smsPlatXhr.getDisabledValue(1))