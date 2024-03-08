package interfacepack.bean.hospital;

import java.io.Serializable;
import java.util.Date;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * 护理平台病人住院信息
 * @author leaf
 *
 */
@SuppressWarnings("serial")
@Entity
@Table(name = "INPATIENTS")
public class HLPTPInHosInfo implements Serializable {
	@Id
	@Column(name = "PAT_INDEX_NO")
	@JsonProperty("PATIENT_UID")
	private String uid;
	
	/**
	 * 病人id
	 */
	@Column(name = "PATIENT_ID")
	@JsonProperty("PATIENTID")
	private String patientId;

    /**
     * 病人姓名
     */
    @Column(name = "NAME")
    @JsonProperty("NAME")
    private String patientName;

    /**
     * 性别
     */
    @Column(name = "PHYSI_SEX_NAME")
    @JsonProperty("SEX")
    private String sex;

    /**
     * 年龄
     */
    @Column(name = "AGE")
    @JsonProperty("AGE")
    private String age;

    /**
	 * 住院次数
	 */
	@Column(name = "SERIES")
	@JsonProperty("SERIES")
	private Integer series;
	
	/**
	 * 病历号
	 */
	@Column(name = "MRN")
	@JsonProperty("MRN")
	private String mrn;
	
	/**
	 * 床位号
	 */
	@Column(name = "BED_NO")
	@JsonProperty("BEDNO")
	private String bedNo;
	
	/**
	 * 生日
	 */
	@Column(name = "BIRTH_DATE")
	@JsonProperty("BIRTHDAY")
	private Date birthday;
	
	/**
	 * 病区code
	 */
	@Column(name = "WARD_CODE")
	@JsonProperty("WARDCODE")
	private String wardCode;
	
	/**
	 * 病区name
	 */
	@Column(name = "WARD_NAME")
	@JsonProperty("WARDNAME")
	private String wardName;
	
	/**
	 * 科室code
	 */
	@Column(name = "DEPT_CODE")
	@JsonProperty("DEPTCODE")
	private String deptCode;
	
	/**
	 * 科室name
	 */
	@Column(name = "DEPT_NAME")
	@JsonProperty("DEPTNAME")
	private String deptName;
	
	/**
	 * 入院时间
	 */
	@Column(name = "ADMISSION_TIME")
	@JsonProperty("INADMITTIME")
	private Date inAdmitTime;	
	
	/**
	 * 入科时间
	 */
	@Column(name = "ADMISSION_WARD_TIME")
	@JsonProperty("INWARDTIME")
	private Date inWardTime;
	
	/**
	 * 诊断
	 */
	@Column(name = "DIAGNOSIS_NAME")
	@JsonProperty("DIAGNOSIS")
	private String diagnosis;
	
	/**
	 * 护理级别
	 */
	@Column(name = "NURSING_CLASS")
	@JsonProperty("NURSINGLEVEL")
	private String nursingLevel;
	
	/**
	 * 医保类别
	 */
	@Column(name = "CHARGE_TYPE_NAME")
	@JsonProperty("INSURANCETYPE")
	private String insuranceType;
	
	/**
	 * 总费用
	 */
	@Column(name = "TOTAL_COST")
	@JsonProperty("SUMCOST")
	private Float sumCost;
	
	/**
	 * 预交金
	 */
	@Column(name = "PRE_PAYMENT")
	@JsonProperty("PREPAYMENTS")
	private Float prePayments;
	
	/**
	 * 自付费用
	 */
	@Column(name = "SELF_PAYMENT")
	@JsonProperty("SELFPAYMENTS")
	private Float selfPayments;
	
	/**
	 * 欠费标志(0:不欠费;1:欠费)
	 */
	@Column(name = "ARREAR_FLAG")
	@JsonProperty("ARREAR")
	private Integer arrear;
	
	/**
	 * 饮食医嘱
	 */
	@Column(name = "DIET")
	@JsonProperty("FOODHABIT")
	private String foodHabit;
	
	/**
	 * 过敏史
	 */
	@Column(name = "ALLERGY")
	@JsonProperty("ALLERGY")
	private String allergy;
	
	/**
	 * 主治医生姓名
	 */
	@Column(name = "ATTEND_DR_NAME")
	@JsonProperty("ATTNDOCTOR")
	private String attnDoctor;
	
	/**
	 * 出院时间
	 */
	@Column(name = "DISCHARGE_DATE")
	@JsonProperty("OUTADMITTIME")
	private Date outAdmitTime;
	
	/**
	 * 病人状态(住院,出院)
	 */
	@Column(name = "STATUS")
	@JsonProperty("STATUS")
	private String status;

	@Column(name = "name")
	private String name;
	
	@ManyToOne(cascade = { CascadeType.ALL })
	@JoinColumn(name="MRN", referencedColumnName="MRN", insertable = false, updatable = false)
	private HLPTPBasicInfo basicInfo;
	
	/**
	 * 责任护士工号
	 */
	@Column(name = "PRIMARY_NURSE_CODE")
	@JsonProperty("PRIMARYNURSECODE")
	private String primaryNurseCode;
	
	/**
	 * 责任护士姓名
	 */
	@Column(name = "PRIMARY_NURSE_NAME")
	@JsonProperty("PRIMARYNURSENAME")
	private String primaryNurseName;

	/**
	 * 责任护士姓名
	 */
	@Column(name = "PATIENT_PATHOGENETIC_CONDITION")
	@JsonProperty("PATIENTPATHOGENETICCONDITION")
	private String patientPathogeneticCondition;

	public String getPatientPathogeneticCondition() {
		return patientPathogeneticCondition;
	}

	public void setPatientPathogeneticCondition(String patientPathogeneticCondition) {
		this.patientPathogeneticCondition = patientPathogeneticCondition;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getUid() {
		return uid;
	}

	public void setUid(String uid) {
		this.uid = uid;
	}

	public String getPatientId() {
		return patientId;
	}

	public void setPatientId(String patientId) {
		this.patientId = patientId;
	}

	public Integer getSeries() {
		return series;
	}

	public void setSeries(Integer series) {
		this.series = series;
	}

	public String getMrn() {
		return mrn;
	}

	public void setMrn(String mrn) {
		this.mrn = mrn;
	}

	public String getBedNo() {
		return bedNo;
	}

	public void setBedNo(String bedNo) {
		this.bedNo = bedNo;
	}

	public Date getBirthday() {
		return birthday;
	}

	public void setBirthday(Date birthday) {
		this.birthday = birthday;
	}

	public String getWardCode() {
		return wardCode;
	}

	public void setWardCode(String wardCode) {
		this.wardCode = wardCode;
	}

	public String getWardName() {
		return wardName;
	}

	public void setWardName(String wardName) {
		this.wardName = wardName;
	}

	public String getDeptCode() {
		return deptCode;
	}

	public void setDeptCode(String deptCode) {
		this.deptCode = deptCode;
	}

	public String getDeptName() {
		return deptName;
	}

	public void setDeptName(String deptName) {
		this.deptName = deptName;
	}

	public Date getInAdmitTime() {
		return inAdmitTime;
	}

	public void setInAdmitTime(Date inAdmitTime) {
		this.inAdmitTime = inAdmitTime;
	}

	public Date getInWardTime() {
		return inWardTime;
	}

	public void setInWardTime(Date inWardTime) {
		this.inWardTime = inWardTime;
	}

	public String getDiagnosis() {
		return diagnosis;
	}

	public void setDiagnosis(String diagnosis) {
		this.diagnosis = diagnosis;
	}

	public String getNursingLevel() {
		return nursingLevel;
	}

	public void setNursingLevel(String nursingLevel) {
		this.nursingLevel = nursingLevel;
	}

	public String getInsuranceType() {
		return insuranceType;
	}

	public void setInsuranceType(String insuranceType) {
		this.insuranceType = insuranceType;
	}

	public Float getSumCost() {
		return sumCost;
	}

	public void setSumCost(Float sumCost) {
		this.sumCost = sumCost;
	}

	public Float getPrePayments() {
		return prePayments;
	}

	public void setPrePayments(Float prePayments) {
		this.prePayments = prePayments;
	}

	public Float getSelfPayments() {
		return selfPayments;
	}

	public void setSelfPayments(Float selfPayments) {
		this.selfPayments = selfPayments;
	}

	public Integer getArrear() {
		return arrear;
	}

	public void setArrear(Integer arrear) {
		this.arrear = arrear;
	}

	public String getFoodHabit() {
		return foodHabit;
	}

	public void setFoodHabit(String foodHabit) {
		this.foodHabit = foodHabit;
	}

	public String getAllergy() {
		return allergy;
	}

	public void setAllergy(String allergy) {
		this.allergy = allergy;
	}

	public String getAttnDoctor() {
		return attnDoctor;
	}

	public void setAttnDoctor(String attnDoctor) {
		this.attnDoctor = attnDoctor;
	}

	public Date getOutAdmitTime() {
		return outAdmitTime;
	}

	public void setOutAdmitTime(Date outAdmitTime) {
		this.outAdmitTime = outAdmitTime;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public HLPTPBasicInfo getBasicInfo() {
		return basicInfo;
	}

	public void setBasicInfo(HLPTPBasicInfo basicInfo) {
		this.basicInfo = basicInfo;
	}

	public String getPrimaryNurseCode() {
		return primaryNurseCode;
	}

	public void setPrimaryNurseCode(String primaryNurseCode) {
		this.primaryNurseCode = primaryNurseCode;
	}

	public String getPrimaryNurseName() {
		return primaryNurseName;
	}

	public void setPrimaryNurseName(String primaryNurseName) {
		this.primaryNurseName = primaryNurseName;
	}

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getPatientName() {
        return patientName;
    }

    public void setPatientName(String patientName) {
        this.patientName = patientName;
    }
}
