package cc.ewell.mcs.duct.bean.duct;


import cc.ewell.mcs.duct.bean.dict.DuctDict;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;
import java.util.List;

/**
 * @author 徐顺洁
 * @date 2023年12月25日 15:54:17
 **/
@Data
@Entity
@Table(name = "MCS_DUCT_INFO")
public class DuctInfo implements Serializable {

    private static final long serialVersionUID = 1626239441432L;

    @Id
    @ApiModelProperty(name = "id" , value = "主键")
    @Column(name = "ID")
    private String id;

    @ApiModelProperty(name = "code" , value = "'导管编码'")
    @Column(name = "CODE")
    private String code;

    @ApiModelProperty(name = "name" , value = "'导管名称'")
    @Column(name = "NAME")
    private String name;

    @ApiModelProperty(name = "type" , value = "'1、本科室置管；2、带入'")
    @Column(name = "TYPE")
    private String type;

    @ApiModelProperty(name = "wardCode" , value = "'置管科室编码'")
    @Column(name = "WARD_CODE")
    private String wardCode;

    @ApiModelProperty(name = "wardName" , value = "'置管科室名称'")
    @Column(name = "WARD_NAME")
    private String wardName;

    @ApiModelProperty(name = "setTimes" , value = "'置管次数：1、首次；'")
    @Column(name = "SET_TIMES")
    private String setTimes;

    @ApiModelProperty(name = "planType" , value = "'1、计划性；2、非计划性（须填原因）'")
    @Column(name = "PLAN_TYPE")
    private String planType;

    @ApiModelProperty(name = "reason" , value = "'非计划性原因'")
    @Column(name = "REASON")
    private String reason;

    @ApiModelProperty(name = "patientUid" , value = "'病人uid'")
    @Column(name = "PATIENT_UID")
    private String patientUid;

    @ApiModelProperty(name = "patientName" , value = "'病人name'")
    @Column(name = "PATIENT_NAME")
    private String patientName;

    @ApiModelProperty(name = "docFormId" , value = "'关联文书记录ID'")
    @Column(name = "DOC_FORM_ID")
    private String docFormId;

    @ApiModelProperty(name = "setDate" , value = "'置管时间'")
    @Column(name = "SET_DATE")
    private Date setDate;

    @ApiModelProperty(name = "remark" , value = "'备注'")
    @Column(name = "REMARK")
    private String remark;

    @ApiModelProperty(name = "position" , value = "'部位'")
    @Column(name = "POSITION")
    private String position;

    @ApiModelProperty(name = "length" , value = "'长度'")
    @Column(name = "LENGTH")
    private Integer length;

    @ApiModelProperty(name = "checkDate" , value = "'核对时间'")
    @Column(name = "CHECK_DATE")
    private Date checkDate;

    @ApiModelProperty(name = "checkBy" , value = "'核对人工号'")
    @Column(name = "CHECK_BY")
    private String checkBy;

    @ApiModelProperty(name = "checkName" , value = "'核对人'")
    @Column(name = "CHECK_NAME")
    private String checkName;

    @ApiModelProperty(name = "takeOutType" , value = "'拔管类型'")
    @Column(name = "TAKE_OUT_TYPE")
    private String takeOutType;

    @ApiModelProperty(name = "takeOutTime" , value = "'拔管时间'")
    @Column(name = "TAKE_OUT_TIME")
    private Date takeOutTime;

    @ApiModelProperty(name = "takeOutReason" , value = "'拔管原因'")
    @Column(name = "TAKE_OUT_REASON")
    private String takeOutReason;

    @ApiModelProperty(name = "takeOutAuditBy" , value = "'拔管审核人工号'")
    @Column(name = "TAKE_OUT_AUDIT_BY")
    private String takeOutAuditBy;

    @ApiModelProperty(name = "takeOutAuditName" , value = "'拔管审核人'")
    @Column(name = "TAKE_OUT_AUDIT_NAME")
    private String takeOutAuditName;

    @ApiModelProperty(name = "isValid" , value = "'1、正常；0、删除'")
    @Column(name = "IS_VALID")
    private int isValid;

    @ApiModelProperty(name = "createBy" , value = "'创建人工号'")
    @Column(name = "CREATE_BY")
    private String createBy;

    @ApiModelProperty(name = "createName" , value = "'创建人'")
    @Column(name = "CREATE_NAME")
    private String createName;

    @ApiModelProperty(name = "createDate" , value = "'创建时间'")
    @Column(name = "CREATE_DATE")
    private Date createDate;

    @ApiModelProperty(name = "lastUpdatedBy" , value = "'最后更新人工号'")
    @Column(name = "LAST_UPDATED_BY")
    private String lastUpdatedBy;

    @ApiModelProperty(name = "lastUpdatedName" , value = "'最后更新人'")
    @Column(name = "LAST_UPDATED_NAME")
    private String lastUpdatedName;

    @ApiModelProperty(name = "lastUpdatedDate" , value = "'最后更新时间'")
    @Column(name = "LAST_UPDATED_DATE")
    private Date lastUpdatedDate;

    @Transient
    private DuctDict dict;

    @Transient
    private List<DuctRecord> records;

}
