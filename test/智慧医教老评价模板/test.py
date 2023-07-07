import requests

type = 12

data = {"1": {"command": "turnevaluate/getevaluatebytype", "sessionid": "174d41ef374b482cd8205edc14eea151", "loginid": "1", "type": f"{type}"}}

json = requests.post("http://localhost:8080/mx-service/turnevaluate/getevaluatebytype", json=data).json()

multiselectdict = {
    1: "单选",
    2: "多选",
    4: "填空"
}
typedict = {
    1: "住院医评价带教老师",
    4: "带教老师评价住院医",
    5: "住院医评价科室",
    12: "护士长评价",
}
beanlist = json['1']['beanlist']
with open("{}.docx".format(typedict[type]), "w", encoding="utf-8") as f:
    for result in beanlist:
        multiselect = result['multiselect']
        title = result['title'] + " " + "({})".format(multiselectdict[multiselect])
        print(title)
        f.write(title)
        f.write("\n\n")
        print()
        itemlist = result['itemlist']
        for item in itemlist:
            content = item['content']
            score = item['score']
            if type == 12:
                score = item['evascore']
            cs = content + " (分值：{})".format(score)
            print(cs)
            f.write(cs+"\n")
        f.write("\n")
        print()
