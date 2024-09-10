package com.bozhong.nursestaff.module.domain;

import lombok.Getter;
import lombok.Setter;

import java.util.Date;

@Getter
@Setter
public class NurseWorkExperienceDO extends BaseEditStatusDO{

    private String nurseId;

    private Integer auditStatus;

    private Integer type;

    private String wardName;

    private String workplace;

    private String level;

    private String title;

    private String position;

    private String witness;

    private String witnessPhone;

    private String remark;

    private Date startDate;

    private Date endDate;

    private Integer validFlag;

    private String createId;

    private Date createTime;

    private String updateId;

    private Date updateTime;

    private String icuFlag;

    private String deptProperty;

    private String custom1;
    private String custom2;
    private String custom3;
    private String custom4;
    private String custom5;

    /**
     * 离职时职务
     */
    private String resignationPosition;

}