
# -*- coding: gbk -*-


import re
with open("DDL.sql", "r") as f:
    ddl = f.read()
cdict = {}
for column in ddl.split("\n"):
    r = re.findall("\((\d+)\)", column)
    if len(r) > 0:
        co = column
        c = ""
        x = False
        for char in co:
            if char == " ":
                if x:
                    break
                continue
            else:
                c = c + char
                x = True
        cdict[c] = r[0]
# print(cdict)
#
with open('test.txt', "r", encoding='utf-8') as f:
    x = f.read()
with open('text2.txt', "r", encoding='utf-8') as f:
    y = f.read()
l = x.split(", ")
l2 = y.split(", ")
for i1,i2 in zip(l, l2):
    print(i1,"\t"+ i2,"\t"+ str(len(i2.replace("(String)", "").replace("(Integer)", "").replace("(Double)", ""))) if i2 is not None and i2 != 'null' else 0, cdict[i1] if i1 in cdict else '0', "--------------------------------------------" if (len(i2.replace("(String)", "").replace("(Integer)", "").replace("(Double)", "")) if i2 is not None and i2 != 'null' else 0) > (int(cdict[i1]) if i1 in cdict else 0) else "")

with open('text3.txt', "r", encoding='utf-8') as f:
    sqllog = f.read()


# score_result = re.findall(".*, (\[\{\".*?\"\}\])\(String\),", sqllog)
# for score in score_result:
#     print(score, len(score), cdict['SCORE_CONTENT'])
