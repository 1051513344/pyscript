
from translate import Translator

content = "1-场地,2-药品,3-题目主干,4-OSCE考试指引,5-咨询管理附件,6-在线资源链接,7-门(Doors)"

dict = {
    "题目主干": "SubjectTrunk"
}

for i in content.split(","):
    type = i.split("-")[0]
    name = i.split("-")[1]
    print(f'xxx("{name}", {type}),')