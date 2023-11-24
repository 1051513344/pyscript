
# -*- coding:gbk -*-
import os
import shutil
import codecs
import re
from scripts.util import ymalUtil

if __name__ == "__main__":

    dataConfigPath = "D:\DataConfig"
    projectPath = "D:\workspace"
    # -------------------------------------------������--------------------------------------------------- #
    contextPath = "NIS_TianjinZYeryuan"  # tomcat ����Ŀ���ֶ�ָ��context
    projectName = "��������ҽԺ�ƶ�����"
    # -------------------------------------------������--------------------------------------------------- #

    DataConfig = dataConfigPath + "\\" + contextPath
    server = projectPath + "\\" + projectName + "\\" + "server"
    resources = server + "\\" + contextPath + "\src\main\\resources\\resources.properties"
    resources = resources if os.path.exists(resources) else server + "\src\main\\resources\\resources.properties"
    resources_inner_yml = server + "\\" + contextPath + "\src\main\\resources\config\\resources_inner.yml"
    resources_inner_yml = resources_inner_yml if os.path.exists(resources_inner_yml) else server + "\src\main\\resources\config\\resources_inner.yml"

    if os.path.exists(resources_inner_yml):
        # springboot����Ŀ�Զ���ȡyml�����е�context
        contextPath = ymalUtil.read_yml(resources_inner_yml)["server"]["servlet.context-path"].replace("/", "")

    print(f"contextPath: {contextPath}")

    # ����DataConfig��������
    if os.path.exists(DataConfig) is False:
        os.mkdir(DataConfig)
        conf = DataConfig + "\\" + "conf"
        if os.path.exists(conf) is False:
            os.mkdir(conf)
            if os.path.exists(server):
                if os.path.exists(resources):
                    shutil.copy(resources, conf)

    # ����PCָ���ַ
    # -------------------------------------------������--------------------------------------------------- #
    serverPort = "8080"
    # -------------------------------------------������--------------------------------------------------- #
    projectRootPath = projectPath + "\\" + projectName
    PCpath = ""
    for dir in os.listdir(projectRootPath):
        if dir.startswith("PC_"):
            PCpath = dir
    PCexePath = ""
    if PCpath != "":
        PCexePath = projectRootPath+"\\"+PCpath
        if os.path.exists(PCexePath):
            MCSPC_xml = PCexePath+"\\" + "MCSPC.xml"
            if os.path.exists(MCSPC_xml):
                with open(MCSPC_xml, "r", encoding="utf-8-sig") as f:
                    config_xml = f.read()
                    find_server_urls = re.findall("<serverUrl>(.*)</serverUrl>", config_xml)
                    config_server_url = find_server_urls[0] if len(find_server_urls) > 0 else None
                    if config_server_url is not None:
                        config_xml = config_xml.replace(config_server_url, f"http://10.111.1.160:{serverPort}/{contextPath}/")
                    else:
                        print("serverUrl����δ�ҵ���")
                if config_server_url is not None:
                    shutil.copy(MCSPC_xml, MCSPC_xml.replace("MCSPC.xml", "MCSPC-bak.xml"))
                    with open(MCSPC_xml, "w", encoding="utf-8-sig") as f:
                        f.write(config_xml)