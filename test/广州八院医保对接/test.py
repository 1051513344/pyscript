


import re

def to_camelcase(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)

def to_underscore(name: str) -> str:
    """驼峰转下划线"""
    if '_' not in name:
        name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    else:
        raise ValueError(f'{name}字符中包含下划线，无法转换')
    return name.lower()


def getEn(text):
    return text.replace(getZh(text), "").strip()

def getZh(text):
    return re.findall('[\u4e00-\u9fa5].*', text)[0]

if __name__ == "__main__":
    pass
    # 【生成字段及注释】
    # param = """
    #     mdtrt_cert_type	就诊凭证类型
    #     mdtrt_cert_no	就诊凭证编号
    #     orgin_card_info	读卡原始信息
    #     sign	读卡签名
    #     card_sn	卡识别码
    #     begntime	开始时间
    #     psn_cert_type	人员证件类型
    #     certno	证件号码
    #     psn_name	人员姓名
    # """
    # for p in param.split("\n"):
    #     if p.startswith("        "):
    #         input_param = to_camelcase(getEn(p))
    #         input_param_desc = getZh(p).strip()
    #         print("@ApiModelProperty(value = \"{}\")".format(input_param_desc))
    #         print("private String {};".format(input_param))
    #         print()

    # 【根据原文件为注解添加hidden属性并生成新的java文件】
#     param = """
# 收费批次号
# 处方号
# 单次剂量描述
# 使用频次描述
# 用药周期天数
# 用药途径描述
# 医疗目录编码
# 受单科室编码
# 受单科室名称
# 受单医生编码
# 受单医生姓名
# 外检医院编码
# 不进行审核说明
# 医疗机构目录名称
#     """
#     file = "NetOutPatientCostDetailUploadDto"
#     with open("{}.java".format(file), "r", encoding="utf8") as f:
#         java_content = f.read()
#
#     for p in param.split("\n"):
#         if p is not "" and p is not "    ":
#             desc = "@ApiModelProperty(value = \"{}\")".format(p)
#             java_content = java_content.replace(desc, "@ApiModelProperty(value = \"{}\", hidden = true)".format(p))
#
#     with open("{}-new.java".format(file), "w", encoding="utf8") as f:
#          f.write(java_content)

    # 【添加@JSONField注解（String类型）】
    # param = """
    # @ApiModelProperty(value = "就诊凭证类型")
    # private String mdtrtCertType;
    #
    # @ApiModelProperty(value = "就诊凭证编号")
    # private String mdtrtCertNo;
    #
    # @ApiModelProperty(value = "读卡原始信息", hidden = true)
    # private String orginCardInfo;
    #
    # @ApiModelProperty(value = "读卡签名", hidden = true)
    # private String sign;
    #
    # @ApiModelProperty(value = "卡识别码", hidden = true)
    # private String cardSn;
    #
    # @ApiModelProperty(value = "开始时间", hidden = true)
    # private String begntime;
    #
    # @ApiModelProperty(value = "人员证件类型", hidden = true)
    # private String psnCertType;
    #
    # @ApiModelProperty(value = "证件号码", hidden = true)
    # private String certno;
    #
    # @ApiModelProperty(value = "人员姓名", hidden = true)
    # private String psnName;
    # """
    #
    # hidden = False
    # for p in param.split("\n"):
    #     if p.startswith("    @ApiModelProperty"):
    #         if "hidden" in p:
    #             hidden = True
    #         print(p)
    #     if p.startswith("    private String "):
    #         field = p.replace("    private String ", "").replace(";", "")
    #         if not hidden:
    #             print("    @JSONField(name = \"{}\")".format(to_underscore(field)))
    #         print(p)
    #         print()
    #         hidden = False

    # 【添加@JSONField注解（非String类型）】
    # param = """
    # @ApiModelProperty(value = "就诊信息")
    # private NetOutpatientRegistrationMdtrtinfoDto mdtrtInfo;
    #
    # @ApiModelProperty(value = "代办人信息")
    # private NetOutpatientRegistrationAgnterinfoDto agnterInfo;
    # """
    # for p in param.split("\n"):
    #     if p.startswith("    @ApiModelProperty"):
    #         print(p)
    #     if len(re.findall("    private .* (.*);", p)) > 0:
    #         field = re.findall("    private .* (.*);", p)[0].lower()
    #         print("    @JSONField(name = \"{}\")".format(to_underscore(field)))
    #         print(p)
    #         print()

