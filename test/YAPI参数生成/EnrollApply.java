package cn.ucmed.yijiao.enrolltrain.domain;

import java.util.Date;
import java.io.Serializable;
import lombok.Data;
import lombok.experimental.Accessors;
import com.baomidou.mybatisplus.annotation.*;

@TableName("enroll_apply")
@Data
@Accessors(chain = true)
public class EnrollApply implements Serializable {

    private static final long serialVersionUID=1L;

    /**
     * 主键id
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    /**
     * 创建时间
     */
    private Date createTime;

    /**
     * 修改时间
     */
    private Date updateTime;

    /**
     * 删除时间（非空为删除）
     */
    private String deleteTime;

    /**
     * 招录id
     */
    private Integer enrollId;

    /**
     * 姓名
     */
    private String name;

    /**
     * 照片
     */
    private String photo;

    /**
     * 手机号
     */
    private String phone;

    /**
     * 邮箱
     */
    private String email;

    /**
     * 身份证
     */
    private String idCard;

    /**
     * 国籍
     */
    private String nationality;

    /**
     * 名族
     */
    private String nation;

    /**
     * 家庭地址
     */
    private String familyAddress;

    /**
     * 工作单位
     */
    private String workUnit;

    /**
     * 最高学历 Level表 stud_degree对应的key
     */
    private String highestEducation;

    /**
     * 毕业学校
     */
    private String graduationSchool;

    /**
     * 毕业年份
     */
    private String graduationYear;

    /**
     * 毕业专业
     */
    private String graduationMajor;

    /**
     * 学位，Level -> degree -> key
     */
    private String degree;

    /**
     * 学位类型： Level -> degreetype -> key
     */
    private String degreeType;

    /**
     * 执业资格证照片，array
     */
    private String qualificationCertificateImg;

    /**
     * 执业资格证编号
     */
    private String qualificationCertificateNo;

    /**
     * 执业资格证获取时间
     */
    private Date qualificationCertificateObtainTime;

    /**
     * 1资料预审待审核  2资料预审通过  3资料预审不通过  4现场审核待审核 5现场审核通过  6现场审核不通过 7待录取  8录取  9不录取
     */
    private Integer applyStatus;

    /**
     * 招录用户id
     */
    private Integer advancedUserId;

    /**
     * 资料预审理由
     */
    private String preAuditReason;

    /**
     * 资料预审时间
     */
    private Date preAuditTime;

    /**
     * 资料预审人
     */
    private String preAuditBy;

    /**
     * 现场审核理由
     */
    private String sceneAuditReason;

    /**
     * 现场审核时间
     */
    private Date sceneAuditTime;

    /**
     * 现场审核人
     */
    private String sceneAuditBy;

    /**
     * 录取时间
     */
    private Date enrollAuditTime;

    /**
     * 录取人
     */
    private String enrollAuditBy;

    /**
     * 考试成绩
     */
    private Double score;

    /**
     * 通知状态  1未通知  2已通知
     */
    private Integer notifyStatus;


}
