from scripts.util import convertUtil

columns = """
id
job_number
education
education_number
education_type
start_date
endn_date
school
major
education_degree
education_degree_num
education_date
url
degree_url
operate_time
"""




if __name__ == "__main__":

    className = "Education"

    columns = [i for i in columns.split("\n") if i != ""]

    propertyList = ""

    for column in columns:
        property = convertUtil.name_convert(column.lower())
        propertyList = propertyList + f"    private String {property};"
        if len(columns) - 1 != columns.index(column):
            propertyList = propertyList + "\n\n"

    model = """package com.bozhong.nursetransfer.domain;

import lombok.Getter;
import lombok.Setter;

/**
 * @author 徐顺洁
 * @date 2024年08月15日 14:22:26
 */
@Getter
@Setter
public class {className}DO {open}

{propery}

{close}""".format(className=className, propery=propertyList, open="{", close="}")
    with open(f"{className}DO.java", "w", encoding='utf-8') as f:
        f.write(model)