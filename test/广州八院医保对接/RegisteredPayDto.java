package com.ucmed.unified.dto.thirdParty.wechatMedicarePay;

import com.alibaba.fastjson.annotation.JSONField;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author xushunjie
 * @date 2022-12-21 11:49:53
 */
@Data
public class RegisteredPayDto {

    @ApiModelProperty(value = "支付类型")
    @JSONField(name = "order_type")
    private String orderType;

    @ApiModelProperty(value = "公众帐号id")
    @JSONField(name = "appid")
    private String appid;

    @ApiModelProperty(value = "商户号")
    @JSONField(name = "mch_id")
    private String mchId;

    @ApiModelProperty(value = "第三方服务商订单号")
    @JSONField(name = "hosp_out_trade_no")
    private String hospOutTradeNo;

    @ApiModelProperty(value = "医院名称")
    @JSONField(name = "hospital_name")
    private String hospitalName;

    @ApiModelProperty(value = "随机字符串")
    @JSONField(name = "nonce_str")
    private String nonceStr;

    @ApiModelProperty(value = "总共需要支付现金金额")
    @JSONField(name = "total_fee")
    private Integer totalFee;

    @ApiModelProperty(value = "现金需要支付的金额")
    @JSONField(name = "cash_fee")
    private Integer cashFee;

    @ApiModelProperty(value = "是否允许预结算费用发生变化")
    @JSONField(name = "allow_fee_change")
    private Integer allowFeeChange;

    @ApiModelProperty(value = "用户端ip")
    @JSONField(name = "spbill_create_ip")
    private String spbillCreateIp;

    @ApiModelProperty(value = "回调url")
    @JSONField(name = "notify_url")
    private String notifyUrl;

    @ApiModelProperty(value = "商品描述")
    @JSONField(name = "body")
    private String body;

    @ApiModelProperty(value = "支付后回跳的页面，不论成功或者失败均会回跳")
    @JSONField(name = "return_url")
    private String returnUrl;

    @ApiModelProperty(value = "支付方式")
    @JSONField(name = "pay_type")
    private Integer payType;

    @ApiModelProperty(value = "城市ID")
    @JSONField(name = "city_id")
    private String cityId;

    @ApiModelProperty(value = "医保支付金额")
    @JSONField(name = "insurance_fee")
    private Integer insuranceFee;

    @ApiModelProperty(value = "证件类型")
    @JSONField(name = "user_card_type")
    private Integer userCardType;

    @ApiModelProperty(value = "证件号码")
    @JSONField(name = "user_card_no")
    private String userCardNo;

    @ApiModelProperty(value = "真实姓名")
    @JSONField(name = "user_name")
    private String userName;

    @ApiModelProperty(value = "医保标识")
    @JSONField(name = "is_dept")
    private String isDept;

    @ApiModelProperty(value = "医院HIS系统订单号")
    @JSONField(name = "serial_no")
    private String serialNo;

    @ApiModelProperty(value = "医疗机构编码（医保局分配给机构）")
    @JSONField(name = "org_no")
    private String orgNo;

    @ApiModelProperty(value = "医院下单时间")
    @JSONField(name = "gmt_out_create")
    private String gmtOutCreate;

    @ApiModelProperty(value = "参考医保结构体（医疗机构透传医保）")
    @JSONField(name = "request_content")
    private String requestContent;

    @ApiModelProperty(value = "业务单据号")
    @JSONField(name = "bill_no")
    private String billNo;

    @ApiModelProperty(value = "签名")
    @JSONField(name = "sign")
    private String sign;
}