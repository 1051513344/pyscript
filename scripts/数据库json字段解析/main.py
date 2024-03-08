

with open("data.txt", "r", encoding='utf-8') as f:
    data = f.read()
with open("datas.txt", "r", encoding='utf-8') as f:
    data2 = f.read()



if __name__ == "__main__":

    import json
    total = 0
    for d in data.split("\n"):
        if d == "INSERT INTO MY_TABLE(SCORE_CONTENT) VALUES (null);":
            continue
        score_content = d.replace("INSERT INTO MY_TABLE(SCORE_CONTENT) VALUES ('", "").replace("');", "").replace("\"\"", "\"").replace('"remark":",', '"remark":"",')
        print(score_content)
        score_content_json = json.loads(score_content)
        for i in score_content_json:
            if "4.人文关怀或沟通不到位" == i['scoreReason']:
                total = total + 1
    print(total)


    # total = 0
    # for d in data2.split("\n"):
    #     count = int(d.replace("INSERT INTO MY_TABLE(X) VALUES (", "").replace(");", "").replace("INSERT INTO MY_TABLE(ALLTIMES) VALUES (", ""))
    #     total = total + count
    # print(total)
    #
    # with open("result.json", "r", encoding='utf-8') as f:
    #     result = f.read()
    # resultJSON = json.loads(result)
    # data = resultJSON['data']
    # list = data['list']
    # for i in list:
    #     contentId = i['contentId']
    #     existIssueList = i['existIssueList']
    #     total = 0
    #     for existIssue in existIssueList:
    #         existIssueNum = existIssue['existIssueNum']
    #         total = total + existIssueNum
    #     print(contentId, total)
