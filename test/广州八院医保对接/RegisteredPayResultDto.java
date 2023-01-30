package com.ucmed.unified.dto.thirdParty.wechatMedicarePay;

import com.alibaba.fastjson.annotation.JSONField;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author xushunjie
 * @date 2022-12-22 18:09:53
 */
@Data
public class RegisteredPayResultDto {

    @ApiModelProperty(value = "随机字符串")
    @JSONField(name = "nonce_str")
    private String nonceStr;

    @ApiModelProperty(value = "公众账号ID")
    @JSONField(name = "appid")
    private String appid;

    @ApiModelProperty(value = "签名")
    @JSONField(name = "sign")
    private String sign;

    @ApiModelProperty(value = "错误代码")
    @JSONField(name = "err_code")
    private String errCode;

    @ApiModelProperty(value = "支付小程序")
    @JSONField(name = "pay_appid")
    private String payAppid;

    @ApiModelProperty(value = "业务结果")
    @JSONField(name = "result_code")
    private String resultCode;

    @ApiModelProperty(value = "子商户公众账号ID")
    @JSONField(name = "sub_appid")
    private String subAppid;

    @ApiModelProperty(value = "商户号")
    @JSONField(name = "mch_id")
    private String mchId;

    @ApiModelProperty(value = "子商户号")
    @JSONField(name = "sub_mch_id")
    private String subMchId;

    @ApiModelProperty(value = "返回状态码")
    @JSONField(name = "return_code")
    private String returnCode;

    @ApiModelProperty(value = "诊疗单id")
    @JSONField(name = "med_trans_id")
    private String medTransId;

    @ApiModelProperty(value = "支付链接")
    @JSONField(name = "pay_url")
    private String payUrl;
}