package com.bozhong.schedule.dto.schedule.request;

import java.util.Date;
import lombok.Getter;
import lombok.Setter;
import com.bozhong.schedule.dto.BaseReqDTO;

/**
* @author 徐顺洁
* @since 2024-08-26 13:41:20
*/
@Getter
@Setter
public class ScheduleShiftAuditRecordReqDTO extends BaseReqDTO {


    private String id;
    /**
     * 护士ID
     */
    private String nurseId;
    /**
     * 护士工号
     */
    private String jobNumber;
    /**
     * 护士姓名
     */
    private String name;
    /**
     * 病区ID
     */
    private String unitId;
    /**
     * 解除开始日期
     */
    private Date startTime;
    /**
     * 解除结束日期
     */
    private Date endTime;
    /**
     * 理由
     */
    private String reason;
    /**
     * 审核状态：0：默认待审核 1：通过 2：不通过
     */
    private Integer auditStatus;
    /**
     * 审核人ID
     */
    private String auditId;
    /**
     * 审核人姓名
     */
    private String auditBy;
    /**
     * 审核时间
     */
    private Date auditTime;
    /**
     * 调动类型
     */
    private Integer shiftType;
    /**
     * 申请者ID
     */
    private String createId;
    /**
     * 申请者
     */
    private String createBy;
    /**
     * 申请时间
     */
    private Date createTime;
    /**
     * 更新人ID
     */
    private String updateId;
    /**
     * 更新人姓名
     */
    private String updateBy;
    /**
     * 更新时间
     */
    private Date updateTime;

    private Integer validFlag;

    private Integer pageNum;

    private Integer pageSize;

    @Override
    public void validation() {

    }
}

