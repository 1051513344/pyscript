# -*- coding: gbk -*-
import  re

with open("originXmlInParam.xml", "r", encoding='utf-8') as f:
    originXmlInParam = f.read()
def xmlParse():
    pattern = re.compile('<soap:Body><.*xmlns="http://ws.nis.ewell/">(.*)</.*></soap:Body></soap:Envelope>')
    xmlInParam = pattern.search(originXmlInParam).group(1).replace(' xmlns=""', '').replace(' xsi:nil="true" ', '')
    for param in re.findall('(<.*?>.*?</.*?>)', xmlInParam):
        singleParams = re.findall("<.*?/>", param)
        if len(singleParams) > 0:
            for singleParam in singleParams:
                print("         " + singleParam)
                param = param.replace(singleParam, "")
        else:
            print("         " + param)
def xmlParseForAndroid():
    pattern = re.compile('<v:Body><.*xmlns:n3="http://ws.nis.ewell/">(.*)</.*></v:Body></v:Envelope>')
    xmlInParam = pattern.search(originXmlInParam).group(1).replace(' i:type="d:string"', '').replace(' i:type="d:int"', '').replace(' i:type="d:boolean"', '').replace(' i:type="d:anyType"', '')
    for param in re.findall('(<.*?>.*?</.*?>)', xmlInParam):
        singleParams = re.findall("<.*?/>", param)
        if len(singleParams) > 0:
            for singleParam in singleParams:
                print("         " + singleParam)
                param = param.replace(singleParam, "")
        else:
            print("         " + param)
def main():
    # xmlParse()
    xmlParseForAndroid()


if __name__ == "__main__":

    main()
