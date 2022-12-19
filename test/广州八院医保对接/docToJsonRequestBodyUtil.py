import re

def to_camelcase(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'(_[a-z])', lambda x: x.group(1)[1].upper(), name)

if __name__ == "__main__":
    pass

    param_info = """
feedetl_sn
psn_no
mdtrt_id
chrg_bchno
rxno
rx_circ_flag
fee_ocur_time
cnt
pric
det_item_fee_sumamt
sin_dos_dscr
used_frqu_dscr
prd_days
medc_way_dscr
med_list_codg
medins_list_codg
bilg_dept_codg
bilg_dept_name
bilg_dr_codg
bilg_dr_name
acord_dept_codg
acord_dept_name
orders_dr_code
orders_dr_name
hosp_appr_flag
tcmdrug_used_way
etip_flag
etip_hosp_code
dscg_tkdrug_flag
matn_fee_flag
unchk_flag
unchk_memo
medins_list_name
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
    # 填充属性
    for param, require in zip(param_info_list, require_info_list):
        if require.strip() is "Y":
            print("	\"{}\": \"1\",".format(param.strip()))
    print("=================================================")
    print()

    print("=================================================")
    for param, require in zip(param_info_list, require_info_list):
        if require.strip() is "Y":
            print('param.put("{}", {});'.format(param.strip(), to_camelcase(param.strip())))
    print("=================================================")
    print()

    s = ''
    for param, require in zip(param_info_list, require_info_list):
        if require.strip() is "Y":
            s = s + 'String {}'.format(to_camelcase(param.strip())) + ", "
    print("=================================================")
    print(s)
    print("=================================================")
    print()

    # print("=================================================")
    # for param, require in zip(param_info_list, require_info_list):
    #     if require.strip() is "Y":
    #         params = param.split("\t")
    #         print("     * @param {} {}".format(to_camelcase(params[0]), params[1]))
    # print("=================================================")
    # print()

    print("=================================================")
    for param, require in zip(param_info_list, require_info_list):
        if require.strip() is "Y":
            print("String {} = null;".format(to_camelcase(param)))
    print("=================================================")
    print()

    print("=================================================")
    s = ''
    for param, require in zip(param_info_list, require_info_list):
        if require.strip() is "Y":
            s = s + "{}, ".format(to_camelcase(param))
    print(s)
    print("=================================================")
    print()
