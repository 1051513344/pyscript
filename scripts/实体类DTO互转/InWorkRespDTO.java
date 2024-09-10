package com.bozhong.nursetransfer.common.dto.resp;

import com.bozhong.nursetransfer.common.dto.BaseRespDTO;
import lombok.Getter;
import lombok.Setter;
import java.util.Date;

/**
 * @author 徐顺洁
 * @date 2024年08月15日 14:22:26
 */
@Getter
@Setter
public class InWorkRespDTO extends BaseRespDTO {

    private String id;

    private String jobNumber;

    private String nurseId;

    private String outUnitId;

    private String unitId;

    private Date startDate;

    private Date endnDate;

    private String witness;

    private Date operateTime;

}