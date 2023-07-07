package cn.ucmed.yijiao.base.domain.dto;

import lombok.Data;

@Data
public class StudentsIdTxtConvert {
    /**
     * 住培年级
     */
    private Integer turngrade;

    /**
     * 住培年级
     */
    private String turngradeTxt;

    /**
     * 所属院区id
     */
    private Integer hospitalId;

    /**
     * 所属院区id 显示
     */
    private String hospitalIdTxt;
}
