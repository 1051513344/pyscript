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
    table_name = "project_format"
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
    project_format_dict = {}
    for r in result:
        project_format_dict[r['format']] = r['id']

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
    building_standard_dict = {}


    for format, project_format_id in project_format_dict.items():
        for r in result:
            if r['project_format_id'] == project_format_id:
                building_standard_dict[format+"-"+r['standard']] = r['id']

    table_name = "item"
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
    item_dict = {}
    for format_standard, building_standard_id in building_standard_dict.items():
        for r in result:
            if r['building_standard_id'] == building_standard_id:
                item_dict[format_standard+"-"+r['name']] = r['id']

    table_name = "item_detail"
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
    item_detail_dict = {}
    for format_standard_item, item_id in item_dict.items():
        for r in result:
            if r['item_id'] == item_id:
                item_detail_dict[format_standard_item + "-" + r['name']] = r['id']



    image_config_dict = {
        "年照明": 20,
        "年办公设备": 22,
        "年天然气": 22,
        "年医疗设备": 22,
        "年电器设备": 22,
        "年空调设备": 22,
        "年室内用水": 24,
        "年室外用水": 25,
        "年冷却塔用水": 25
    }

    print(item_dict)

    with open("detail.js", "r", encoding='utf-8') as f:
        detail = f.read()

    detailDataJson = json.loads(detail)

    for project_format, v in detailDataJson.items():

        energyCacheDict = None
        waterCacheDict = None
        for building_standard, v2 in v.items():

            if isinstance(v2, dict):
                for energyDataType, v3 in v2['energy'].items():
                    name = v3['title'].replace("用能减量约", "").replace("减量约", "")
                    title = v3['title']
                    unit = v3['unit']
                    standard = building_standard
                    if building_standard == '国际':
                        standard = '绿建'

                    # 批量导入项详细配置
                    # key = project_format + "-" + standard + "-" + "年节能"
                    # print("INSERT INTO `green_building_quotation`.`item_detail` (`name`, `is_deleted`, `create_time`, `update_time`, `item_id`, `image_config_id`, `title`, `unit`) VALUES ('{}', 0, NOW(), NOW(), {}, {}, '{}', '{}');".format(name, item_dict[key], image_config_dict[name], title, unit))

                    # 批量导入图片属性配置
                    logoWidth = v3['logoWidth']
                    logoHeight = v3['logoHeight']
                    logoTop = v3['logoTop']
                    logoLeft = v3['logoLeft']
                    key = project_format + "-" + standard + "-" + "年节能" + "-" + name
                    print("INSERT INTO `green_building_quotation`.`image_attr_config` (`rpx_width`, `rpx_height`, `rpx_top`, `rpx_left`, `is_deleted`, `create_time`, `update_time`, `building_standard_id`, `item_id`, `item_detail_id`) VALUES ({}, {}, {}, {}, 0, NOW(), NOW(), NULL, NULL, {});".format(logoWidth, logoHeight, logoTop, logoLeft, item_detail_dict[key]))
                energyCacheDict = v2['energy']
            else:
                if v2.startswith("$"):
                    for energyDataType, v3 in energyCacheDict.items():
                        name = v3['title'].replace("用能减量约", "").replace("减量约", "")
                        title = v3['title']
                        unit = v3['unit']
                        standard = building_standard
                        if building_standard == '国际':
                            standard = '绿建'

                        # 批量导入项详细配置
                        # key = project_format + "-" + standard + "-" + "年节能"
                        # print(
                        #     "INSERT INTO `green_building_quotation`.`item_detail` (`name`, `is_deleted`, `create_time`, `update_time`, `item_id`, `image_config_id`, `title`, `unit`) VALUES ('{}', 0, NOW(), NOW(), {}, {}, '{}', '{}');".format(
                        #         name, item_dict[key], image_config_dict[name], title, unit))

                        # 批量导入图片属性配置
                        logoWidth = v3['logoWidth']
                        logoHeight = v3['logoHeight']
                        logoTop = v3['logoTop']
                        logoLeft = v3['logoLeft']
                        key = project_format + "-" + standard + "-" + "年节能" + "-" + name
                        print(
                            "INSERT INTO `green_building_quotation`.`image_attr_config` (`rpx_width`, `rpx_height`, `rpx_top`, `rpx_left`, `is_deleted`, `create_time`, `update_time`, `building_standard_id`, `item_id`, `item_detail_id`) VALUES ({}, {}, {}, {}, 0, NOW(), NOW(), NULL, NULL, {});".format(
                                logoWidth, logoHeight, logoTop, logoLeft, item_detail_dict[key]))
            if isinstance(v2, dict):
                for waterDataType, v3 in v2['water'].items():
                    name = v3['title'].replace("用能减量约", "").replace("减量约", "")
                    title = v3['title']
                    unit = v3['unit']
                    standard = building_standard
                    if building_standard == '国际':
                        standard = '绿建'
                    # 批量导入项详细配置
                    # key = project_format + "-" + standard + "-" + "年节水"
                    # print(
                    #     "INSERT INTO `green_building_quotation`.`item_detail` (`name`, `is_deleted`, `create_time`, `update_time`, `item_id`, `image_config_id`, `title`, `unit`) VALUES ('{}', 0, NOW(), NOW(), {}, {}, '{}', '{}');".format(
                    #         name, item_dict[key], image_config_dict[name], title, unit))
                    # 批量导入图片属性配置
                    logoWidth = v3['logoWidth']
                    logoHeight = v3['logoHeight']
                    logoTop = v3['logoTop']
                    logoLeft = v3['logoLeft']
                    key = project_format + "-" + standard + "-" + "年节水" + "-" + name
                    print(
                        "INSERT INTO `green_building_quotation`.`image_attr_config` (`rpx_width`, `rpx_height`, `rpx_top`, `rpx_left`, `is_deleted`, `create_time`, `update_time`, `building_standard_id`, `item_id`, `item_detail_id`) VALUES ({}, {}, {}, {}, 0, NOW(), NOW(), NULL, NULL, {});".format(
                            logoWidth, logoHeight, logoTop, logoLeft, item_detail_dict[key]))
                waterCacheDict = v2['water']
            else:
                if v2.startswith("$"):
                    for waterDataType, v3 in waterCacheDict.items():
                        name = v3['title'].replace("用能减量约", "").replace("减量约", "")
                        title = v3['title']
                        unit = v3['unit']
                        standard = building_standard
                        if building_standard == '国际':
                            standard = '绿建'

                        # 批量导入项详细配置
                        # key = project_format + "-" + standard + "-" + "年节水"
                        # print(
                        #     "INSERT INTO `green_building_quotation`.`item_detail` (`name`, `is_deleted`, `create_time`, `update_time`, `item_id`, `image_config_id`, `title`, `unit`) VALUES ('{}', 0, NOW(), NOW(), {}, {}, '{}', '{}');".format(
                        #         name, item_dict[key], image_config_dict[name], title, unit))

                        # 批量导入图片属性配置
                        logoWidth = v3['logoWidth']
                        logoHeight = v3['logoHeight']
                        logoTop = v3['logoTop']
                        logoLeft = v3['logoLeft']
                        key = project_format + "-" + standard + "-" + "年节水" + "-" + name
                        print(
                            "INSERT INTO `green_building_quotation`.`image_attr_config` (`rpx_width`, `rpx_height`, `rpx_top`, `rpx_left`, `is_deleted`, `create_time`, `update_time`, `building_standard_id`, `item_id`, `item_detail_id`) VALUES ({}, {}, {}, {}, 0, NOW(), NOW(), NULL, NULL, {});".format(
                                logoWidth, logoHeight, logoTop, logoLeft, item_detail_dict[key]))



