#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

class Dnconsole:
    '''
    【雷电控制台类】
    version: 9.0
    import该文件会自动实例化为 Dc
    '''

    def __init__( self, installation_path:str ):
        '''
        【构造方法】
        '''
        # if 模拟器安装路径存在性检测
        if os.path.exists(installation_path) is False:
            print('模拟器安装路径不存在！')
        # 获取模拟器安装路径
        self.ins_path = installation_path
        # Dnconsole程序路径
        self.console_path = self.ins_path + r'\ldconsole.exe '
        # if Dnconsole程序路径检测
        if os.path.exists(self.console_path) is False:
            print('Dnconsole程序路径不存在！\n请确认模拟器安装文件是否完整或模拟器版本是否不符！')
        # adb程序路径
        self.adb_path = self.ins_path + r'\adb.exe '
        # if adb程序路径检测
        if os.path.exists(self.adb_path) is False:
            print('Dnconsole程序路径不存在！\n请确认模拟器安装文件是否完整！')
        # 模拟器截屏程序路径
        self.screencap_path = r'/system/bin/screencap'
        # 模拟器截图保存路径
        self.devicess_path = r'/sdcard/autosS.png'
        # 本地图片保存路径
        self.images_path = r'D:\PycharmWorkspace\images'
        # 构造完成
        print('Class-Dnconsole is ready.(%s)' % (self.ins_path))
    def CMD( self, cmd:str ):
        '''
        【执行控制台命令语句】
        :param cmd: 命令
        :return: 控制台调试内容
        '''
        CMD = self.console_path + cmd # 控制台命令
        process = os.popen(CMD)
        result = process.read()
        process.close()
        return result

    def reboot( self, index:int = 0 ):
        '''
        【重启模拟器】
        :param index: 模拟器序号
        :return: 控制台调试内容
        '''
        cmd = 'reboot --index %d' %(index)
        return self.CMD(cmd)


if __name__ == "__main__":

    dnconsole = Dnconsole("D:\雷电模拟器\leidian\LDPlayer9")
    dnconsole.reboot(0)