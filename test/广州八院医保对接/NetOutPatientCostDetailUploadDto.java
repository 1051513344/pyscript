package com.ucmed.unified.dto.thirdParty.healthInsuranceHis;

import com.alibaba.fastjson.annotation.JSONField;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author xushunjie
 * @date 2022/12/15 13:45
 */
@Data
public class NetOutPatientCostDetailUploadDto {

    @ApiModelProperty(value = "费用明细流水号")
    @JSONField(name = "feedetl_sn")
    private String feedetlSn;

    @ApiModelProperty(value = "人员编号")
    @JSONField(name = "psn_no")
    private String psnNo;

    @ApiModelProperty(value = "就诊ID")
    @JSONField(name = "mdtrt_id")
    private String mdtrtId;

    @ApiModelProperty(value = "收费批次号")
    private String chrgBchno;

    @ApiModelProperty(value = "处方号")
    private String rxno;

    @ApiModelProperty(value = "外购处方标志")
    @JSONField(name = "rx_circ_flag")
    private String rxCircFlag;

    @ApiModelProperty(value = "费用发生日期")
    @JSONField(name = "fee_ocur_time")
    private String feeOcurTime;

    @ApiModelProperty(value = "数量")
    @JSONField(name = "cnt")
    private String cnt;

    @ApiModelProperty(value = "单价")
    @JSONField(name = "pric")
    private String pric;

    @ApiModelProperty(value = "明细项目费用总额")
    @JSONField(name = "det_item_fee_sumamt")
    private String detItemFeeSumamt;

    @ApiModelProperty(value = "单次剂量描述")
    private String sinDosDscr;

    @ApiModelProperty(value = "使用频次描述")
    private String usedFrquDscr;

    @ApiModelProperty(value = "用药周期天数")
    private String prdDays;

    @ApiModelProperty(value = "用药途径描述")
    private String medcWayDscr;

    @ApiModelProperty(value = "医疗目录编码")
    @JSONField(name = "med_list_codg")
    private String medListCodg;

    @ApiModelProperty(value = "医疗机构目录编码")
    @JSONField(name = "medins_list_codg")
    private String medinsListCodg;

    @ApiModelProperty(value = "开单科室编码")
    @JSONField(name = "bilg_dept_codg")
    private String bilgDeptCodg;

    @ApiModelProperty(value = "开单科室名称")
    @JSONField(name = "bilg_dept_name")
    private String bilgDeptName;

    @ApiModelProperty(value = "开单医生编码")
    @JSONField(name = "bilg_dr_codg")
    private String bilgDrCodg;

    @ApiModelProperty(value = "开单医生姓名")
    @JSONField(name = "bilg_dr_name")
    private String bilgDrName;

    @ApiModelProperty(value = "受单科室编码")
    private String acordDeptCodg;

    @ApiModelProperty(value = "受单科室名称")
    private String acordDeptName;

    @ApiModelProperty(value = "受单医生编码")
    private String ordersDrCode;

    @ApiModelProperty(value = "受单医生姓名")
    private String ordersDrName;

    @ApiModelProperty(value = "医院审批标志")
    @JSONField(name = "hosp_appr_flag")
    private String hospApprFlag;

    @ApiModelProperty(value = "中药使用方式")
    @JSONField(name = "tcmdrug_used_way")
    private String tcmdrugUsedWay;

    @ApiModelProperty(value = "外检标志")
    @JSONField(name = "etip_flag")
    private String etipFlag;

    @ApiModelProperty(value = "外检医院编码")
    private String etipHospCode;

    @ApiModelProperty(value = "出院带药标志")
    @JSONField(name = "dscg_tkdrug_flag")
    private String dscgTkdrugFlag;

    @ApiModelProperty(value = "生育费用标志")
    @JSONField(name = "matn_fee_flag")
    private String matnFeeFlag;

    @ApiModelProperty(value = "不进行审核标志")
    @JSONField(name = "unchk_flag")
    private String unchkFlag;

    @ApiModelProperty(value = "不进行审核说明")
    private String unchkMemo;

    @ApiModelProperty(value = "医疗机构目录名称")
    private String medinsListName;

}
