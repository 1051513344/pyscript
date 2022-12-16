import re
import time

def to_camelcase(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)

data_type_dict = {
    '字符型': 'String',
    '数值型': 'Integer',
    '日期型': 'Date'
}


if __name__ == "__main__":
    pass

    param_info = """
mdtrt_cert_type	就诊凭证类型	字符型
mdtrt_cert_no	就诊凭证编号	字符型
orgin_card_info	读卡原始信息	字符型
sign	读卡签名	字符型
card_sn	卡识别码	字符型
begntime	开始时间	日期型
psn_cert_type	人员证件类型	字符型
certno	证件号码	字符型
psn_name	人员姓名	字符型
    """
    require_info = """
Y
Y







    """
    param_info_list = [p for p in param_info.split("\n") if not p.startswith("    ") and p is not ""]
    require_info_list = require_info.split("\n")[1:-1]

    package = input("请输入包名：")
    className = input("请输入类名：")
    author = "xushunjie"
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("{}.java".format(className), "w", encoding="utf-8") as f:
        f.write(package+"\n\n")
        f.write("import com.alibaba.fastjson.annotation.JSONField;\n")
        f.write("import io.swagger.annotations.ApiModelProperty;\n")
        f.write("import lombok.Data;\n")
        f.write("\n")
        f.write("/**\n * @author {}\n * @date {}\n */\n".format(author, date))
        f.write("@Data\n")
        f.write("public class " + className + " {\n")
        # 填充属性
        for param,require in zip(param_info_list, require_info_list):
            params = param.split("\t")
            if require is "Y":
                f.write("\n")
                f.write("    @ApiModelProperty(value = \"{}\")\n".format(params[1]))
                f.write("    @JSONField(name = \"{}\")\n".format(params[0]))
                f.write("    private {} {};".format(data_type_dict[params[2]], to_camelcase(params[0])))
            else:
                f.write("\n")
                f.write("    @ApiModelProperty(value = \"{}\", hidden = true)\n".format(params[1]))
                f.write("    private {} {};".format(data_type_dict[params[2]], to_camelcase(params[0])))
            f.write("\n")
        f.write("}")
