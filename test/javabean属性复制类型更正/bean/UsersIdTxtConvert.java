package cn.ucmed.yijiao.base.domain.dto;

import lombok.Data;

@Data
public class UsersIdTxtConvert {
    /**
     * 性别(0=>男，1=>女)
     */
    private Integer sex;

    private String sexTxt;

    /**
     * 证件类型:0身份证 1其他
     */
    private Integer cardType;

    /**
     * 证件类型:0身份证 1其他  显示用
     */
    private String cardTypeTxt;

    /**
     * 民族
     */
    private String nation;

    /**
     * 民族信息
     */
    private String nationTxt;

    /**
     * 国家
     */
    private String nationality;

    /**
     * 国家值
     */
    private String nationalityTxt;

    /**
     * 职称 对应Level.code=title 记录的id
     */
    private Integer professional;

    /**
     * 职称 对应Level.code=title 记录的id 显示用
     */
    private String professionalTxt;

    /**
     * 学历 对应Level.code=education 记录的id
     */
    private Integer educational;

    /**
     * 学历 对应Level.code=education 记录的id 显示用
     */
    private String educationalTxt;

    /**
     * 医院等级[] 对应Level.code=hospital 记录的id
     */
    private Integer hospitalLevel;

    /**
     * 医院等级[] 对应Level.code=hospital 记录的id 显示用
     */
    private String hospitalLevelTxt;

    /**
     * 学位  对应Level.code=degree 记录的id
     */
    private Integer degree;

    /**
     * 学位  对应Level.code=degree 记录的id
     */
    private String degreeTxt;

    /**
     * 学位类型（专业型，科研型）
     */
    private Integer degreeType;

    /**
     * 学位类型（专业型，科研型 degreetype）
     */
    private String degreeTypeTxt;

    /**
     * 数据来源 0：技能中心 1：住院医 2：实习生 3：教务系统同步 4:注册审批 5:大赛
     */
    private Integer source;

    /**
     * 数据来源 0：技能中心 1：住院医 2：实习生 3：教务系统同步 4:注册审批 5:大赛
     */
    private String sourceTxt;

    /**
     * 班级编号 对应行政班Classes.id
     */
    private Integer stdClassId;

    /**
     * 班级编号 对应行政班Classes.id
     */
    private String stdClassIdTxt;

    /**
     * 班级
     */
    private String stdClassTxt;

    /**
     * 学员身份类别 住培生；实习生；学生
     */
    private String studentType;

    /**
     * 学员身份类别 住培生；实习生；学生
     */
    private String studentTypeTxt;
}
