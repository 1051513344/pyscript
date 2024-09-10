from scripts.util import convertUtil

columns = """
id
job_number
name
code
unit_id
issue_date
remark
operate_time
"""




if __name__ == "__main__":
    className = "Duty"
    viewName = "v_yh_hl_duty"

    columns = [i for i in columns.split("\n") if i != ""]

    resultList = ""
    Base_Column_List = ""

    for column in columns:
        property = convertUtil.name_convert(column.lower())
        resultList = resultList + f'        <result column="{column}" property="{property}" jdbcType="VARCHAR"/>'
        Base_Column_List = Base_Column_List + "        " + f"{column}"
        if len(columns) - 1 != columns.index(column):
            resultList = resultList + "\n"
            Base_Column_List = Base_Column_List + ",\n"

    mapper = f"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<mapper namespace="com.bozhong.nursetransfer.mapper.hr.{className}Mapper">
    <resultMap id="BaseResultMap" type="com.bozhong.nursetransfer.domain.{className}">
{resultList}
    </resultMap>

    <sql id="Base_Column_List">
{Base_Column_List}
    </sql>
    
    <sql id="Table_Name">
        {viewName}
    </sql>

    <select id="selectByWhere" resultMap="BaseResultMap" parameterType="java.util.HashMap">
        select
        <include refid="Base_Column_List"/>
        from <include refid="Table_Name"/>
    </select>
</mapper>"""
    with open(f"{className}Mapper.xml", "w", encoding='utf-8') as f:
        f.write(mapper)