
import json

with open("1.json", "r", encoding="utf-8") as f:
    a = f.read()

with open("2.json", "r", encoding="utf-8") as f:
    b = f.read()

jsona = json.loads(a)
jsonb = json.loads(b)





if __name__ == "__main__":
    totalRowCount = 0
    for i in jsona:
        if 'nurseScheduleRespDTOList' in i:
            totalRowCount = totalRowCount + len(i['nurseScheduleRespDTOList'])
    print(totalRowCount)
    # print(len(jsona))
    # print(len(jsonb))

