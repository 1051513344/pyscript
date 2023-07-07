package cn.ucmed.yijiao.base.domain.dto;

import lombok.Data;

@Data
public class StdEducationIdTxtConvert {

    private String bachelorMajor;

    private String bachelorMajorTxt;

    private String bachelorDegree;

    private String bachelorDegreeTxt;

    private String bachelorDegreeType;

    private String bachelorDegreeTypeTxt;


    private String masterMajor;

    private String masterMajorTxt;

    private String masterDegree;

    private String masterDegreeTxt;

    private String masterDegreeType;

    private String masterDegreeTypeTxt;


    private String doctorMajor;

    private String doctorMajorTxt;

    private String doctorDegree;

    private String doctorDegreeTxt;

    private String doctorDegreeType;

    private String doctorDegreeTypeTxt;

    /**
     * level表中关联id
     */
    private String levelPrimary;

}
