package cn.ucmed.yijiao.enrolltrain.domain.bo;

import java.util.Date;
import java.io.Serializable;
import java.util.List;

import cn.ucmed.yijiao.common.core.validate.AddGroup;
import cn.ucmed.yijiao.common.core.validate.EditGroup;
import lombok.Data;
import lombok.experimental.Accessors;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Data
@Accessors(chain = true)
public class EnrollApplyBo implements Serializable {

    private static final long serialVersionUID=1L;

    /**
     * 主键id
     */
    @NotNull(message = "主键id不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer id;

    /**
     * 创建时间
     */
    @NotNull(message = "创建时间不能为空", groups = { AddGroup.class, EditGroup.class })
    private Date createTime;

    /**
     * 修改时间
     */
    @NotNull(message = "修改时间不能为空", groups = { AddGroup.class, EditGroup.class })
    private Date updateTime;

    /**
     * 删除时间（非空为删除）
     */
    @NotBlank(message = "删除时间（非空为删除）不能为空", groups = { AddGroup.class, EditGroup.class })
    private String deleteTime;

    /**
     * 招录id
     */
    @NotNull(message = "招录id不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer enrollId;

    /**
     * 姓名
     */
    @NotBlank(message = "姓名不能为空", groups = { AddGroup.class, EditGroup.class })
    private String name;

    /**
     * 照片
     */
    @NotBlank(message = "照片不能为空", groups = { AddGroup.class, EditGroup.class })
    private String photo;

    /**
     * 手机号
     */
    @NotBlank(message = "手机号不能为空", groups = { AddGroup.class, EditGroup.class })
    private String phone;

    /**
     * 邮箱
     */
    @NotBlank(message = "邮箱不能为空", groups = { AddGroup.class, EditGroup.class })
    private String email;

    /**
     * 身份证
     */
    @NotBlank(message = "身份证不能为空", groups = { AddGroup.class, EditGroup.class })
    private String idCard;

    /**
     * 性别 1男 2女
     */
    @NotNull(message = "性别 1男 2女不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer sex;

    /**
     * 出生日期
     */
    @NotBlank(message = "出生日期不能为空", groups = { AddGroup.class, EditGroup.class })
    private String birthday;

    /**
     * 国籍
     */
    @NotBlank(message = "国籍不能为空", groups = { AddGroup.class, EditGroup.class })
    private String nationality;

    /**
     * 名族
     */
    @NotBlank(message = "名族不能为空", groups = { AddGroup.class, EditGroup.class })
    private String nation;

    /**
     * 家庭地址
     */
    @NotBlank(message = "家庭地址不能为空", groups = { AddGroup.class, EditGroup.class })
    private String familyAddress;

    /**
     * 工作单位
     */
    @NotBlank(message = "工作单位不能为空", groups = { AddGroup.class, EditGroup.class })
    private String workUnit;

    /**
     * 最高学历 Level表 stud_degree对应的key
     */
    @NotBlank(message = "最高学历 Level表 stud_degree对应的key不能为空", groups = { AddGroup.class, EditGroup.class })
    private String highestEducation;

    /**
     * 毕业学校
     */
    @NotBlank(message = "毕业学校不能为空", groups = { AddGroup.class, EditGroup.class })
    private String graduationSchool;

    /**
     * 毕业年份
     */
    @NotBlank(message = "毕业年份不能为空", groups = { AddGroup.class, EditGroup.class })
    private String graduationYear;

    /**
     * 毕业专业
     */
    @NotBlank(message = "毕业专业不能为空", groups = { AddGroup.class, EditGroup.class })
    private String graduationMajor;

    /**
     * 学位，Level -> degree -> key
     */
    @NotBlank(message = "学位，Level -> degree -> key不能为空", groups = { AddGroup.class, EditGroup.class })
    private String degree;

    /**
     * 学位类型： Level -> degreetype -> key
     */
    @NotBlank(message = "学位类型： Level -> degreetype -> key不能为空", groups = { AddGroup.class, EditGroup.class })
    private String degreeType;

    /**
     * 执业资格证照片，array
     */
    @NotBlank(message = "执业资格证照片，array不能为空", groups = { AddGroup.class, EditGroup.class })
    private List<String> qualificationCertificateImg;

    /**
     * 执业资格证编号
     */
    @NotBlank(message = "执业资格证编号不能为空", groups = { AddGroup.class, EditGroup.class })
    private String qualificationCertificateNo;

    /**
     * 执业资格证获取时间
     */
    @NotNull(message = "执业资格证获取时间不能为空", groups = { AddGroup.class, EditGroup.class })
    private Date qualificationCertificateObtainTime;

    /**
     * 资料预审状态 1 待审核 2 通过 3 不通过
     */
    @NotNull(message = "资料预审状态 1 待审核 2 通过 3 不通过不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer preAuditStatus;

    /**
     * 资料预审理由
     */
    @NotBlank(message = "资料预审理由不能为空", groups = { AddGroup.class, EditGroup.class })
    private String preAuditReason;

    /**
     * 资料预审时间
     */
    @NotNull(message = "资料预审时间不能为空", groups = { AddGroup.class, EditGroup.class })
    private Date preAuditTime;

    /**
     * 资料预审人
     */
    @NotBlank(message = "资料预审人不能为空", groups = { AddGroup.class, EditGroup.class })
    private String preAuditBy;

    /**
     * 现场审核状态 1 待审核 2 通过 3 不通过
     */
    @NotNull(message = "现场审核状态 1 待审核 2 通过 3 不通过不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer sceneAuditStatus;

    /**
     * 现场审核时间
     */
    @NotNull(message = "现场审核时间不能为空", groups = { AddGroup.class, EditGroup.class })
    private Date sceneAuditTime;

    /**
     * 现场审核理由
     */
    @NotBlank(message = "现场审核理由不能为空", groups = { AddGroup.class, EditGroup.class })
    private String sceneAuditReason;

    /**
     * 现场审核人
     */
    @NotBlank(message = "现场审核人不能为空", groups = { AddGroup.class, EditGroup.class })
    private String sceneAuditBy;

    /**
     * 通知状态  1未通知  2已通知
     */
    @NotNull(message = "通知状态  1未通知  2已通知不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer notifyStatus;

    /**
     * 通知时间
     */
    @NotNull(message = "通知时间不能为空", groups = { AddGroup.class, EditGroup.class })
    private Date notifyTime;

    /**
     * 1资料预审待审核  2现场待审核  3资料预审不通过  4现场审核不通过 5 待考试  6待录取  7录取  8不录取
     */
    @NotNull(message = "1资料预审待审核  2现场待审核  3资料预审不通过  4现场审核不通过 5 待考试  6待录取  7录取  8不录取不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer applyStatus;

    /**
     * 招录用户id
     */
    @NotNull(message = "招录用户id不能为空", groups = { AddGroup.class, EditGroup.class })
    private Integer advancedUserId;

    /**
     * 录取时间
     */
    @NotNull(message = "录取时间不能为空", groups = { AddGroup.class, EditGroup.class })
    private Date enrollAuditTime;

    /**
     * 录取人
     */
    @NotBlank(message = "录取人不能为空", groups = { AddGroup.class, EditGroup.class })
    private String enrollAuditBy;

    /**
     * 考试成绩
     */
    @NotNull(message = "考试成绩不能为空", groups = { AddGroup.class, EditGroup.class })
    private Double score;


}
