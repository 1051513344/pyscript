
from sql.query.queryDataFunc import QueryDB
import os
import shutil

if __name__ == "__main__":

    host = "***.***.***.***"
    port = 3306
    user = "root"
    password = "************"
    db = "ucmed2"
    charset = "utf8"
    table_name = "Menus"

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

    objects = [i for i in os.listdir("F:\文件\新医教平台\迭代\迭代八\移动端新UI图标") if "." not in i]
    # 1x 图标
    # for dir in objects:
    #     print(dir)
    #     os.mkdir(dir)
    #     os.chdir(dir)
    #     print("===========================")
    #     pngs = [i for i in os.listdir("F:\文件\新医教平台\迭代\迭代八\移动端新UI图标\\" + dir) if "@" not in i and i.endswith(".png")]
    #     for png in pngs:
    #         pic = ""
    #         if png.endswith("-2.png"):
    #             if os.path.exists("F:\文件\新医教平台\迭代\迭代八\移动端新UI图标\\" + dir + png.replace("-2.png", "") + ".png"):
    #                 pic = png.replace(" ", "").replace("-2.png", "") + ".png"
    #                 print(pic)
    #             else:
    #                 pic = png.replace(" ", "")
    #                 print(pic)
    #         else:
    #             pic = png.replace(" ", "")
    #             print(pic)
    #         shutil.copy("F:\文件\新医教平台\迭代\迭代八\移动端新UI图标\\" + dir + "\\" + pic, "./" + pic.replace("-2.png", ".png").replace("-3.png", ".png"))
    #     print("===========================")
    #     os.chdir("../")

    # 2X 图标
    for dir in objects:
        print(dir)
        os.mkdir(dir)
        os.chdir(dir)
        print("===========================")
        pngs = [i for i in os.listdir("F:\文件\新医教平台\迭代\迭代八\移动端新UI图标\\" + dir) if "@2x" in i and i.endswith(".png")]
        for png in pngs:
            pic = png.replace(" ", "").replace("@2x-1", "").replace("@2x-2", "").replace("@2x-3", "").replace("@2x", "")
            print(pic)
            shutil.copy("F:\文件\新医教平台\迭代\迭代八\移动端新UI图标\\" + dir + "\\" + png, "./" + pic)
        print("===========================")
        os.chdir("../")


    # convert_dict = {
    #     "喇叭": "通知公告",
    #     "资源管理-学生": "资源管理(学生)",
    #     "资源管理-教师": "资源管理(教师)",
    #     "住培轮转-住院医师": "住培轮转-住院医",
    #     "出科审核": "出科考核"
    # }
    #
    # for dir in objects:
    #     print("#"+dir)
    #     os.chdir(dir)
    #     for png in os.listdir("."):
    #         name = png.replace(".png", "")
    #         if name in convert_dict:
    #             name = convert_dict[name]
    #         data = q.queryByCondition(moduleid="futuredoctorapp", name=name)
    #         id = data[0]["id"]
    #         ico = "../../images/futuredoctorapp/new/" + dir + "/" + png
    #         # print(id)
    #         # print(ico)
    #         # print(data)
    #         # print()
    #         print("update Menus set ico = \"{}\" where id = {};".format(ico, id))
    #
    #     os.chdir("../")

    q.connection.close()