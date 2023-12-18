
# -*- coding:gbk -*-
import os
import shutil
import codecs
import re
from scripts.util import ymalUtil

if __name__ == "__main__":

    dataConfigPath = "D:\DataConfig"
    projectPath = "D:\workspace"
    # -------------------------------------------更改项--------------------------------------------------- #
    contextPath = "NIS_Zhangdianrenmin"  # tomcat 老项目须手动指定context
    projectName = "淄博市张店区人民医院-移动护理"
    # -------------------------------------------更改项--------------------------------------------------- #

    DataConfig = dataConfigPath + "\\" + contextPath
    server = projectPath + "\\" + projectName + "\\" + "server"
    resources = server + "\\" + contextPath + "\src\main\\resources\\resources.properties"
    resources = resources if os.path.exists(resources) else server + "\src\main\\resources\\resources.properties"
    resources = resources if os.path.exists(resources) else server + "\\NIS_SE_admin\\src\main\\resources\\resources.properties"
    resources_inner_yml = server + "\\" + contextPath + "\src\main\\resources\config\\resources_inner.yml"
    resources_inner_yml = resources_inner_yml if os.path.exists(resources_inner_yml) else server + "\src\main\\resources\config\\resources_inner.yml"

    if os.path.exists(resources_inner_yml):
        # springboot新项目自动读取yml配置中的context
        contextPath = ymalUtil.read_yml(resources_inner_yml)["server"]["servlet.context-path"].replace("/", "")

    print(f"contextPath: {contextPath}")

    # 替换lombok版本
    pom_xml = server+"\\pom.xml"
    if os.path.exists(pom_xml):
        exist = False
        with open(pom_xml, "r", encoding="utf-8") as f:
            pom_dep_xml = f.read()
            if "<lombok.version>1.18.8</lombok.version>" in pom_dep_xml:
                exist = True
        if exist:
            with open(pom_xml, "w", encoding="utf-8") as f:
                pom_dep_xml = pom_dep_xml.replace("<lombok.version>1.18.8</lombok.version>", "<lombok.version>1.18.24</lombok.version>")
                f.write(pom_dep_xml)

    # 生成DataConfig环境配置
    if os.path.exists(DataConfig) is False:
        os.mkdir(DataConfig)
        conf = DataConfig + "\\" + "conf"
        if os.path.exists(conf) is False:
            os.mkdir(conf)
            if os.path.exists(server):
                if os.path.exists(resources):
                    shutil.copy(resources, conf)
                    conf_resources_properties = conf + "\\resources.properties"
                    with open(conf_resources_properties, "r", encoding="utf-8") as f:
                        resources_properties = f.read()
                    with open(conf_resources_properties, "w", encoding="utf-8") as f:
                        for line in resources_properties.split("\n"):
                            if line.startswith("spring.datasource.url="):
                                f.write("spring.datasource.url=jdbc:oracle:thin:@192.168.10.239:1521:orcl\n")
                            elif line.startswith("spring.redis.host="):
                                f.write("spring.redis.host=127.0.0.1\n")
                            elif line.startswith("spring.redis.port="):
                                f.write("spring.redis.port=7191\n")
                            elif line.startswith("spring.redis.password="):
                                f.write("spring.redis.password=XFQQ\n")
                            else:
                                f.write(line+"\n")

    # 更改PC指向地址
    # -------------------------------------------更改项--------------------------------------------------- #
    serverPort = "8810"
    # -------------------------------------------更改项--------------------------------------------------- #
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
                    find_auto_update = re.findall("<autoUpdate>.*</autoUpdate>", config_xml)
                    config_server_url = find_server_urls[0] if len(find_server_urls) > 0 else None
                    config_auto_update = find_auto_update[0] if len(find_auto_update) > 0 else None
                    if config_server_url is not None:
                        config_xml = config_xml.replace(config_server_url, f"http://10.111.1.160:{serverPort}/{contextPath}/")
                    else:
                        print("serverUrl配置未找到！")
                    if config_auto_update is not None:
                        config_xml = config_xml.replace(config_auto_update, f"<autoUpdate>0</autoUpdate>")
                    else:
                        print("autoUpdate配置未找到！")
                if config_server_url is not None:
                    shutil.copy(MCSPC_xml, MCSPC_xml.replace("MCSPC.xml", "MCSPC-bak.xml"))
                    with open(MCSPC_xml, "w", encoding="utf-8-sig") as f:
                        f.write(config_xml)