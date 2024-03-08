


def toSqlIn(list):
    sql = "("
    for obj in list:
        id  = "'{}',".format(obj['id'])
        sql = sql + id
    sql = sql[:-1] + ")"
    print(sql)

def getStatus(list):
    for obj in list:
        print(obj['status'])

def t(list):
    for obj in list:
        if "最高学历" in obj['aliasName']:
            print(obj)

def t2(obj):
    list = obj['object']['list']
    for o in list:
        for child in o['children']:
            scheduleList = child['scheduleList']
            for schedule in scheduleList:
                nurseScheduleRespDTOList = schedule['nurseScheduleRespDTOList']
                if nurseScheduleRespDTOList is not None:
                    for nurseSchedule in nurseScheduleRespDTOList:
                        print(nurseSchedule)



if __name__ == "__main__":

    import json

    with open("test.json", "r", encoding='utf-8') as f:
        jsonObj = json.loads(f.read())

    # t(jsonObj)
    t2(jsonObj)

