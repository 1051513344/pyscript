# -*- coding: gbk -*-
import  json

with open("参数map.txt", "r", encoding='utf-8') as f:
    paramMap = f.read()

with open("sqlTemplate.txt", "r", encoding='utf-8') as f:
    sqlTemplate = f.read()

def parse():
    # json格式参数解析
    if paramMap.startswith("{"):
        paramJson = json.loads(paramMap)
    else:
        # map格式参数解析 格式：key:value
        paramJson = {}
        for param in paramMap.split("\n"):
            p = param.split(":")
            key = p[0]
            if len(p) == 2:
                value = p[1]
                if value.startswith("["):
                    value = json.loads(value)
                paramJson[key] = value
            else:
                paramJson[key] = ("".join([i+":" for i in p[1:]]))[:-1]
    print(paramJson)
    sqlTemplateBuilder = sqlTemplate
    for k,v in paramJson.items():
        if f":{k}" in sqlTemplate:
            value = ""
            if isinstance(v, list):
                value = str(tuple(v)).replace("(", "").replace(")", "")
            elif "-" and ":" in v:
                value = f"to_date('{v}' , 'yyyy-mm-dd hh24:mi:ss')"
            elif isinstance(v, str):
                value = f"'{v}'"
            else:
                value = f'{v}'
            sqlTemplateBuilder = sqlTemplateBuilder.replace(f":{k}", value)
    print(sqlTemplateBuilder)

def main():
    parse()


if __name__ == "__main__":

    main()