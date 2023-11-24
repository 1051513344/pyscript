# -*- coding:gbk -*-
import yaml

def read_yml(file):
    """读取yml,传入文件路径file"""
    f = open(file,'r',encoding="utf-8")   # 读取文件
    yml_config = yaml.load(f,Loader=yaml.FullLoader)    # Loader为了更加安全

    """Loader的几种加载方式
    BaseLoader - -仅加载最基本的YAML
    SafeLoader - -安全地加载YAML语言的子集。建议用于加载不受信任的输入。
    FullLoader - -加载完整的YAML语言。避免任意代码执行。这是当前（PyYAML5.1）默认加载器调用yaml.load(input)（发出警告后）。
 	UnsafeLoader - -（也称为Loader向后兼容性）原始的Loader代码，可以通过不受信任的数据输入轻松利用。"""
    return yml_config

