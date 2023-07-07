package cn.ucmed.yijiao.base.domain.vo;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.apache.commons.lang3.StringUtils;

import java.util.Date;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ResidentStudentVo {

    private Integer id;

    /**
     * 用户名（登录的账号）
     */
    private String code;

    /**
     * 用户名（登录的账号）
     */
    private String username;

    /**
     * 姓名
     */
    private String name;

    /**
     * 手机号（登录的账号）
     */
    private String mobile;

    /**
     * 紧急联系电话
     */
    private String urgentMobile;

    /**
     * 一卡通
     */
    private String cardno;

    /**
     * 性别(0=>男，1=>女)
     */
    private Integer sex;

    private String studentSex;

    /**
     * 电子邮箱
     */
    private String email;

    /**
     * 状态,0=正常（默认），1=禁止，2=删除
     */
    private Integer status;

    /**
     * 是否学生 0=学生（默认），1=教师（其他）
     */
    private Integer isStd;

    /**
     * 证件类型:0身份证 1其他
     */
    private Integer cardType;

    private String cardTypeTxt;

    /**
     * 证件号码
     */
    private String cardNum;


    /**
     * 记住我 存储登录后的session信息 格式：时间戳.时间戳.session
     */
    private String rememberToken;

    /**
     * 头像地址
     */
    private String imageurl;

    /**
     * 民族
     */
    private String nation;

    private String nationTxt;

    /**
     * 国家
     */
    private String nationality;

    private String nationalityTxt;

    /**
     * 出生日期
     */
    @JsonFormat(pattern = "yyyy-MM-dd")
    private Date birthday;

    /*
     * 工作单位
     * */
    private String workunit;

    /**
     * 毕业后去向
     */
    private String gradDirection;

    /**
     * 家庭住址
     */
    private String homeAddress;

    /**
     * 现住址
     */
    private String currentAddress;

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

    private String educationalTxt;

    /**
     * 医院等级[] 对应Level.code=hospital 记录的id
     */
    private Integer hospitalLevel;

    private String hospitalLevelTxt;

    /**
     * 学位  对应Level.code=degree 记录的id
     */
    private Integer degree;

    private String degreeTxt;

    /**
     * 学位类型（专业型，科研型）
     */
    private Integer degreeType;

    private String degreeTypeTxt;

    /**
     * 禁用原因
     */
    private String forbiddenReason;

    /**
     * 数据来源 0：技能中心 1：住院医 2：实习生 3：教务系统同步 4:注册审批 5:大赛
     */
    private Integer source;

    /**
     * 分享码
     */
    private String sharecode;

    /**
     * 证件照
     */
    private String identityUrl;

    //规培信息

    /**
     * 计划id
     */
    private Integer planId;

    /**
     * 住培医生id
     */
    private Integer stuId;

    /**
     * 培训专业，与level表的主键关联
     */
    private Integer profId;

    private String profIdTxt;

    /**
     * 学员类型，与level表的主键关联
     */
    private Integer typeId;

    private String typeTxt;

    private String studentType;

    /**
     * 专业基地，与level表的主键关联
     */
    private Integer baseId;

    private String baseName;

    /**
     * 导师
     */
    private String tutor;

    /**
     * 导师
     */
    private String teacherId;

    public String getTeacherId() {
        return StringUtils.isBlank(teacherId)?null:teacherId;
    }

    /**
     * 导师
     */
    private String teacherName;

    /**
     * 培训年限核定
     */
    private String verificationYears;

    private String verificationYearsTxt;

    /**
     * 招收年度
     */
    private String recruityear;

    /**
     * 实际培训开始时间
     */
    @JsonFormat(pattern = "yyyy-MM-dd")
    private Date realBeginTime;

    /**
     * 应届/往届,0：应届 1：往届
     */
    private Integer fresh;

    private String freshTxt;

    /**
     * 是否为对口支援计划住院医师, 0：是 1：否
     */
    private Integer partnerAssistance;

    private String partnerAssistanceTxt;

    /**
     * 对口支援计划住院医师送出单位
     */
    private String partnerAssistanceUnit;

    /**
     * 是否执业医师，0：是 1：否
     */
    private Integer practicing;

    private String practicingTxt;

    /**
     * 执业医师资格证号
     */
    private String qualificationNumber;

    /**
     * 结业年度 关联Level表 code:graduationyears
     */
    private Integer graduationYear;

    private String graduationYearTxt;

    //学历信息

    /**
     * 本科毕业院校
     */
    private String bachelorSchool;

    /**
     * 本科毕业年份
     */
    private String bachelorGraduate;

    public String getBachelorGraduate() {
        if (StringUtils.isNotBlank(bachelorGraduate) && bachelorGraduate.length() > 4 && bachelorGraduate.contains("-")) {
            return bachelorGraduate.split("-")[0];
        }
        return bachelorGraduate;
    }

    /**
     * 本科毕业专业
     */
    private String bachelorMajor;

    private String bachelorMajorTxt;

    /**
     * 是否全科订单定向, 0：是     1：否
     */
    private Integer directional;

    private String directionalTxt;

    /**
     * 本科学位
     */
    private String bachelorDegree;

    private String bachelorDegreeTxt;

    /**
     * 是否硕士研究生, 0：是 1：否
     */
    private Integer ismaster;

    /**
     * 硕士研究生毕业院校
     */
    private String masterSchool;

    /**
     * 硕士研究生毕业年份
     */
    private String masterGraduate;

    public String getMasterGraduate() {
        if (StringUtils.isNotBlank(masterGraduate) && masterGraduate.length() > 4 && masterGraduate.contains("-")) {
            return masterGraduate.split("-")[0];
        }
        return masterGraduate;
    }

    /**
     * 硕士研究生毕业专业
     */
    private String masterMajor;

    private String masterMajorTxt;

    /**
     * 硕士研究生学位
     */
    private String masterDegree;

    private String masterDegreeTxt;

    /**
     * 学位类型（硕士）
     */
    private String masterDegreeType;

    private String masterDegreeTypeTxt;

    /**
     * 是否博士生, 0：是 1：否
     */
    private Integer isdoctor;

    /**
     * 博士研究生毕业院校
     */
    private String doctorSchool;

    /**
     * 博士研究生毕业年份
     */
    private String doctorGraduate;

    public String getDoctorGraduate() {
        if (StringUtils.isNotBlank(doctorGraduate) && doctorGraduate.length() > 4 && doctorGraduate.contains("-")) {
            return doctorGraduate.split("-")[0];
        }
        return doctorGraduate;
    }

    /**
     * 博士研究生毕业专业
     */
    private String doctorMajor;

    private String doctorMajorTxt;

    /**
     * 博士研究生学位
     */
    private String doctorDegree;

    private String doctorDegreeTxt;

    /**
     * 学位类型（博士）
     */
    private String doctorDegreeType;

    /**
     * 学位类型（博士）
     */
    private String doctorDegreeTypeTxt;

    /**
     * 班级编号 对应行政班Classes.id
     */
    private Integer stdClassId;

    private String stdClassTxt;

    /**
     * 住培年级
     */
    private Integer turngrade;
    /*
     * 住培年级名字
     * */

    private String turngradeTxt;

    /**
     * 所属院区id
     */
    private Integer hospitalId;

    /**
     * 所属院区id
     */
    private String hospitalIdTxt;

    /**
     * 医院等次
     */
    private String hospitalGrade;

    private String hospitalGradeTxt;

    /**
     * 医院属性，与level表的主键关联
     */
    private Integer hospitalAttributes;

    /*
     * 隶属关系
     * */
    private String hospitalAttributesTxt;

    /**
     * 医院类别，与level表的主键关联
     */
    private Integer hospitalCategory;

    /*
     * 机构级别
     * */

    private String hospitalCategoryTxt;

    /**
     * 是否结业   0：在培   1：结业		2:退培
     */
    private Integer isGraduation;

    /**
     * 是否注册：0-否 1-是
     */
    private Integer isregister;

    /**
     * 是否在协同单位培训, 0：是 1：否
     */
    private Integer cooperative;

    private String cooperativeTxt;


}
