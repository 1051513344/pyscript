package com.bozhong.nursestaff.dto.basics.request;

import java.util.Date;
import com.bozhong.nursestaff.dto.BaseReqDto;
import lombok.Getter;
import lombok.Setter;

/**
* @author 徐顺洁
* @since 2024-08-13 15:54:56
*/
@Getter
@Setter
public class NurseDossierApplyReqDTO extends BaseReqDto {


    private String id;
    /**
     * 工号
     */
    private String jobNumber;
    /**
     * 姓名
     */
    private String name;
    /**
     * 性别
     */
    private String sex;
    /**
     * 手机号
     */
    private String mobile;
    /**
     * 审核状态 0：待审核 1：通过 2：不通过
     */
    private String status;
    /**
     * 申请时间
     */
    private Date applyTime;
    /**
     * 审核人ID
     */
    private String auditId;
    /**
     * 审核人
     */
    private String auditName;
    /**
     * 审核时间
     */
    private Date auditTime;
    /**
     * 创建人ID
     */
    private String createId;
    /**
     * 创建人
     */
    private String createName;
    /**
     * 创建时间
     */
    private Date createTime;
    /**
     * 更新人ID
     */
    private String updateId;
    /**
     * 更新人
     */
    private String updateName;
    /**
     * 更新时间
     */
    private Date updateTime;

    private Integer pageNum;

    private Integer pageSize;

    @Override
    public String paramValidation() {
        return null;
    }
}

