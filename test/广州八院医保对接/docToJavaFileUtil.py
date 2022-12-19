import re
import time

def to_camelcase(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)

data_type_dict = {
    '字符型': 'String',
    '数值型': 'Integer',
    '日期型': 'String'
}


if __name__ == "__main__":


    param_info = """
feedetl_sn	费用明细流水号	字符型
psn_no	人员编号	字符型
mdtrt_id	就诊ID	字符型
chrg_bchno	收费批次号	字符型
rxno	处方号	字符型
rx_circ_flag	外购处方标志	字符型
fee_ocur_time	费用发生日期	日期型
cnt	数量	数值型
pric	单价	数值型
det_item_fee_sumamt	明细项目费用总额	数值型
sin_dos_dscr	单次剂量描述	字符型
used_frqu_dscr	使用频次描述	字符型
prd_days	用药周期天数	数值型
medc_way_dscr	用药途径描述	字符型
med_list_codg	医疗目录编码	字符型
medins_list_codg	医疗机构目录编码	字符型
bilg_dept_codg	开单科室编码	字符型
bilg_dept_name	开单科室名称	字符型
bilg_dr_codg	开单医生编码	字符型
bilg_dr_name	开单医生姓名	字符型
acord_dept_codg	受单科室编码	字符型
acord_dept_name	受单科室名称	字符型
orders_dr_code	受单医生编码	字符型
orders_dr_name	受单医生姓名	字符型
hosp_appr_flag	医院审批标志	字符型
tcmdrug_used_way	中药使用方式	字符型
etip_flag	外检标志	字符型
etip_hosp_code	外检医院编码	字符型
dscg_tkdrug_flag	出院带药标志	字符型
matn_fee_flag	生育费用标志	字符型
unchk_flag	不进行审核标志	字符型
unchk_memo	不进行审核说明	字符型
medins_list_name	医疗机构目录名称	字符型
    """
    require_info = """
Y
Y
Y


Y
Y
Y
Y
Y




Y
Y
Y
Y
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
