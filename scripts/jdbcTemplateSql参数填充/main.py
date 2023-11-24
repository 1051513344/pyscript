# -*- coding: gbk -*-
import  json

with open("参数map.txt", "r", encoding='utf-8') as f:
    paramMap = f.read()

with open("sqlTemplate.txt", "r", encoding='utf-8') as f:
    sqlTemplate = f.read()

def parse():
    paramJson = json.loads(paramMap)
    sqlTemplateBuilder = sqlTemplate
    for k,v in paramJson.items():
        if f":{k}" in sqlTemplate:
            value = ""
            if isinstance(v, list):
                value = str(tuple(v)).replace("(", "").replace(")", "")
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