import re
import time
from sql.query.queryDataFunc import QueryDB
import json


if __name__ == "__main__":

    host = "192.168.56.101"
    port = 3306
    user = "root"
    password = "xsj26875676"
    db = "green_building_quotation"
    charset = "utf8"
    table_name = "building_standard"
    # 获取需要导出的数据
    q = QueryDB(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        table_name=table_name
    )

    result = q.queryAll()

    for r in result:

        print("INSERT INTO `green_building_quotation`.`image_attr_config` (`rpx_width`, `rpx_height`, `rpx_top`, `rpx_left`, `is_deleted`, `create_time`, `update_time`, `building_standard_id`, `item_id`, `item_detail_id`) VALUES (140, 140, 10, 75, 0, NOW(), NOW(), {}, NULL, NULL);".format(r['id']))


