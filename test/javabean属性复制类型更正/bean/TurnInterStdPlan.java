package cn.ucmed.yijiao.base.domain;

import java.util.Date;
import java.io.Serializable;
import lombok.Data;
import lombok.experimental.Accessors;
import com.baomidou.mybatisplus.annotation.*;

@TableName("turn_inter_std_plan")
@Data
@Accessors(chain = true)
public class TurnInterStdPlan implements Serializable {

    private static final long serialVersionUID=1L;

    /**
     * 关联id
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    /**
     * 计划id
     */
    private Integer planId;

    /**
     * 住培医生id
     */
    private Integer stuId;

    /**
     * 委托单位
     */
    private String entrustedUnit;

    /**
     * 培训专业，与level表的主键关联
     */
    private Integer profId;

    /**
     * 学员类型，与level表的主键关联
     */
    private Integer typeId;

    /**
     * 专业基地，与level表的主键关联
     */
    private Integer baseId;

    /**
     * 学员所属科室id，与level表的主键关联
     */
    private Integer deptId;

    /**
     * 硕士学位学科
     */
    private String masterDiscipline;

    /**
     * 导师
     */
    private String tutor;

    /**
     * 住院导师
     */
    private String hospitalTutor;

    /**
     * 应届/往届,0：应届 1：往届
     */
    private Integer fresh;

    /**
     * 是否执业医师，0：是 1：否
     */
    private Integer practicing;

    /**
     * 执业医师资格证号
     */
    private String qualificationNumber;

    /**
     * 是否注册：0-否 1-是
     */
    private Integer isregister;

    /**
     * 实际培训开始时间
     */
    private Date realBeginTime;

    /**
     * 培训年限核定
     */
    private String verificationYears;

    /**
     * 招收年度
     */
    private String recruityear;

    /**
     * 医疗卫生机构
     */
    private Integer medicalUnit;

    /**
     * 医院属性，与level表的主键关联
     */
    private Integer hospitalAttributes;

    /**
     * 医院类别，与level表的主键关联
     */
    private Integer hospitalCategory;

    /**
     * 医院性质，与level表的主键关联
     */
    private Integer hospitalNature;

    /**
     * 医院级别
     */
    private String hospitalLevel;

    /**
     * 医院等次
     */
    private String hospitalGrade;

    /**
     * 基层医疗卫生机构，与level表的主键关联
     */
    private Integer primaryMedical;

    /**
     * 是否在协同单位培训, 0：是 1：否
     */
    private Integer cooperative;

    /**
     * 协同单位
     */
    private String cooperativeUnit;

    /**
     * 协同单位性质，与level表的主键关联
     */
    private Integer cooperativeNature;

    /**
     * 协同医院级别
     */
    private String cooHospitalLevel;

    /**
     * 协同医院等次
     */
    private String cooHospitalGrade;

    /**
     * 协同医院类别
     */
    private String cooHospitalCategory;

    /**
     * 是否为对口支援计划住院医师, 0：是 1：否
     */
    private Integer partnerAssistance;

    /**
     * 对口支援计划住院医师送出单位
     */
    private String partnerAssistanceUnit;

    /**
     * 第一年考核
     */
    private String firstAssessment;

    /**
     * 第二年考核
     */
    private String secondAssessment;

    /**
     * 第三年综合考评
     */
    private String thirdAssessment;

    /**
     * 结业考理论成绩
     */
    private String gradTheoryScore;

    /**
     * 结业考技能成绩
     */
    private String gradSkillScore;

    /**
     * 毕业后去向
     */
    private String gradDirection;

    /**
     * 删除标识（0-正常，1-删除）
     */
    private Integer status;

    /**
     * 结业年度 关联Level表 code:graduationyears
     */
    private Integer graduationYear;

    /**
     * 是否结业   0：在培   1：结业		2:退培
     */
    private Integer isGraduation;

    /**
     * 轮转年级 关联Level表ID code:turngrade
     */
    private Integer turngrade;

    /**
     * 学历 关联level表key字段 code：stud_degree
     */
    private String educational;

    /**
     * 学位 关联level表key字段 code：degree
     */
    private String degree;

    /**
     * 学位类型 关联level表key字段 code：degreetype
     */
    private String degreeType;

    /**
     * 创建时间
     */
    private Date createAt;

    /**
     * 修改时间
     */
    private Date updateAt;

    /**
     * 带教老师
     */
    private String teacherId;


}
