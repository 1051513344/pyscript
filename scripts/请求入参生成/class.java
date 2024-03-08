package com.bozhong.nursestaff.dto.basics.request.meeting;

import com.bozhong.nursestaff.dto.BaseRespDto;
import lombok.Getter;
import lombok.Setter;
import java.util.Date;

/**
 * @author 徐顺洁
 * @date 2024年02月27日 10:12:28
 **/
@Getter
@Setter
public class UpdateReadFileReqDTO extends BaseRespDto {

    private String meetingId;

    private String fileUid;

    private String id;

    private String name;

    private String unitId;

    private String unitName;

    /**
     *  1代表是已读
     *  */
    private Integer read;

    /**
     *  已读时间
     */
    private Date readDate;

}