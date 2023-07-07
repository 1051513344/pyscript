import re
import time
from sql.query.queryDataFunc import QueryDB

def to_camelcase(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)


if __name__ == "__main__":

    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "************"
    db = "ucmed2-base"
    charset = "utf8"
    table_name = "Users"
    # 获取需要导出的数据
    q = QueryDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )
    explainColumnDict = {}
    table_names = ("Users", "Students", "turn_inter_std_plan")
    tableMetaDataDictList = q.queryTableMetaDataDict(table_names)
    for tableMetaDataDict in tableMetaDataDictList:
        explainColumnDict[tableMetaDataDict["COLUMN_COMMENT"]] = tableMetaDataDict["COLUMN_NAME"]




    param_info = """
姓名
所属院区
专业基地
年级
培训状态
状态
    """

    param_info_list = [p for p in param_info.split("\n") if not p.startswith("    ") and p is not ""]

    package = input("请输入包名：")
    if package is None or package == "":
        package = "package cn.ucmed.yijiao.base.domain.bo;"
    className = input("请输入类名：")
    author = "xushunjie"
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("{}.java".format(className), "w", encoding="utf-8") as f:
        f.write(package+"\n\n")
        f.write("import java.io.Serializable;\n")
        f.write("import lombok.Data;\n")
        f.write("import lombok.experimental.Accessors;\n\n")
        f.write("/**\n * @author {}\n * @date {}\n */\n\n".format(author, date))
        f.write("@Data\n")
        f.write("@Accessors(chain = true)\n")
        f.write("public class " + className + " implements Serializable " + "{\n")

        f.write("\n")
        f.write("    private static final long serialVersionUID=1L;\n\n")

        # 过滤重复变量
        propertyList = []

        # 填充属性
        for param in param_info_list:

            if param+"id" in explainColumnDict:
                f.write("    /**\n")
                f.write("     * {}\n".format(param+"id"))
                f.write("     */\n")
                f.write("    private {} {};".format("String", to_camelcase(explainColumnDict[param+"id"])))
                f.write("\n\n")
                propertyList.append(to_camelcase(explainColumnDict[param+"id"]))

                f.write("    /**\n")
                f.write("     * {}\n".format(param + "id").replace("id", ""))
                f.write("     */\n")
                f.write("    private {} {};".format("String", to_camelcase(explainColumnDict[param + "id"]).replace("Id", "")))
                f.write("\n\n")
                propertyList.append(to_camelcase(explainColumnDict[param + "id"]).replace("Id", ""))

            if param in explainColumnDict:
                f.write("    /**\n")
                f.write("     * {}\n".format(param))
                f.write("     */\n")
                f.write("    private {} {};".format("String", to_camelcase(explainColumnDict[param])))
                f.write("\n\n")
                propertyList.append(to_camelcase(explainColumnDict[param]))
            else:
                for k, v in explainColumnDict.items():
                    if param in k and to_camelcase(v) not in propertyList:
                        f.write("    /**\n")
                        f.write("     * {}\n".format(k))
                        f.write("     */\n")
                        f.write("    private {} {};".format("String", to_camelcase(v)))
                        f.write("\n\n")
                        propertyList.append(to_camelcase(v))

        f.write("}")

