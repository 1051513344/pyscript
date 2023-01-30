import re
import time

def to_camelcase(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)

data_type_dict = {
    'String': 'String',
    'string': 'String',
    'Uint': 'Integer',
    'uint': 'Integer',
    'int': 'Integer'
}


if __name__ == "__main__":

    with open("param_info.txt", "r", encoding="utf-8") as f:
        param_info = f.read()
    param_info_list = param_info.split(" ")
    param_list = []
    for p in param_info_list:
        if p is 'Y':
            print(" ".join(param_list[-3:]))
            param_list.clear()
        else:
            param_list.append(p)

    param_info = """
order_type 支付类型 String16
appid 公众帐号id String32
mch_id 商户号 String32
hosp_out_trade_no 第三方服务商订单号 String64
hospital_name 医院名称 string128
nonce_str 随机字符串 String32
total_fee 总共需要支付现金金额 Uint64
cash_fee 现金需要支付的金额 Uint64
allow_fee_change 是否允许预结算费用发生变化 uint8
spbill_create_ip 用户端ip String16
notify_url 回调url String256
body 商品描述 String128
return_url 支付后回跳的页面，不论成功或者失败均会回跳 string128
pay_type 支付方式 uint8
city_id 城市ID String32
insurance_fee 医保支付金额 Uint64
user_card_type 证件类型 Uint8
user_card_no 证件号码 String32
user_name 真实姓名 String32
is_dept 医保标识 String32
serial_no 医院HIS系统订单号 String20
org_no 医疗机构编码（医保局分配给机构） String32
gmt_out_create 医院下单时间 String(14)
request_content 参考医保结构体（医疗机构透传医保） String
bill_no 业务单据号 String20
sign 签名 string32
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
            for k, v in data_type_dict.items():
                if params[2].startswith(k):
                    params[2] = v
            f.write("    private {} {};".format(params[2], to_camelcase(params[0])))
            f.write("\n")
        f.write("}")
