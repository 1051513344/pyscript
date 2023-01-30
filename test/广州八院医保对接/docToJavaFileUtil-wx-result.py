import re
import time
import json

def to_camelcase(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)



if __name__ == "__main__":


    param_info = """
nonce_str 随机字符串
appid 公众账号ID
sign 签名
err_code 错误代码
pay_appid 支付小程序
result_code 业务结果
sub_appid 子商户公众账号ID
mch_id 商户号
sub_mch_id 子商户号
return_code 返回状态码
med_trans_id 诊疗单id
pay_url 支付链接
    """
    param_info_list = [p for p in param_info.split("\n") if not p.startswith("    ") and p is not ""]



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
        for param in param_info_list:
            params = param.split(" ")
            f.write("\n")
            f.write("    @ApiModelProperty(value = \"{}\")\n".format(params[1]))
            f.write("    @JSONField(name = \"{}\")\n".format(params[0]))
            f.write("    private {} {};".format("String", to_camelcase(params[0])))
            f.write("\n")
        f.write("}")
