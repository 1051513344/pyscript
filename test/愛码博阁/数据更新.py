from sql.query.queryDataFunc import *
from sql.update.updateDataFunc import *
import re
def main():
    q = QueryDB(
        "49.235.243.221",
        3306,
        "root",
        "xsj26875676",
        "ssm_blog",
        "utf8mb4",
        "blog"
    )
    print("=========更新前=================")
    result = q.queryAll()
    for i in result:
        print(i["id"])
        # # print(i["content"])
        # matchs = re.search(r'(.*<img src=")(http://)(www.aimaboge.com)(/.*" .*)', i["content"])
        # # print(matchs)
        # if matchs != None:
        #     new_content = i["content"].replace("www.aimaboge.com", "49.235.243.221")
        #     print(new_content)
            # print(i["content"])
            # print(matchs.group(1) + matchs.group(2) + matchs.group(3) + matchs.group(4))
            # print(matchs.group(1).replace("www.aimaboge.com", "49.235.243.221"))
            # part1 = re.sub(r'(.*<img src=")(http://)(www.aimaboge.com)(/.*" .*)', r"\1\2", i["content"])
            # part2 = re.sub(r'(.*<img src=")(http://)(www.aimaboge.com)(/.*" .*)', r"\4", i["content"])
            # new_content = part1 + "49.235.243.221" + part2
            # print(new_content)
            # u = UpdateDB(
            #     "49.235.243.221",
            #     3306,
            #     "root",
            #     "xsj26875676",
            #     "ssm_blog",
            #     "utf8mb4",
            #     "blog"
            # )
            # u.batchUpdate(i["id"], new_content)
            # try:
            #     u.batchUpdate(i["id"], new_content)
            # except Exception as e:
            #     print("更新出错,{},id：".format(e), i["id"])
    # print("=========更新后=================")
    # q = QueryDB(
    #     "49.235.243.221",
    #     3306,
    #     "root",
    #     "xsj26875676",
    #     "ssm_blog",
    #     "utf8mb4",
    #     "blog"
    # )
    # result = q.queryAll("0", "20")
    # for i in result:
    #     print(i["id"])
    #     print(i["content"])


if __name__ == '__main__':
    main()
