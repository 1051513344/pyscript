package com.ucmed.unified.dto.thirdParty.healthInsuranceHis;

import com.alibaba.fastjson.annotation.JSONField;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author xushunjie
 * @date 2022-12-23 16:50:48
 */
@Data
public class OutpatientRegisterCancelDto {

    @ApiModelProperty(value = "就诊ID")
    @JSONField(name = "mdtrt_id")
    private String mdtrtId;

    @ApiModelProperty(value = "人员编号")
    @JSONField(name = "psn_no")
    private String psnNo;

    @ApiModelProperty(value = "住院/门诊号 ")
    @JSONField(name = "ipt_otp_no")
    private String iptOtpNo;

    @ApiModelProperty(value = "就诊方式", hidden = true)
    private String mdtrtMode;
}