# -*- coding:gbk -*-
import yaml

def read_yml(file):
    """��ȡyml,�����ļ�·��file"""
    f = open(file,'r',encoding="utf-8")   # ��ȡ�ļ�
    yml_config = yaml.load(f,Loader=yaml.FullLoader)    # LoaderΪ�˸��Ӱ�ȫ

    """Loader�ļ��ּ��ط�ʽ
    BaseLoader - -�������������YAML
    SafeLoader - -��ȫ�ؼ���YAML���Ե��Ӽ����������ڼ��ز������ε����롣
    FullLoader - -����������YAML���ԡ������������ִ�С����ǵ�ǰ��PyYAML5.1��Ĭ�ϼ���������yaml.load(input)����������󣩡�
 	UnsafeLoader - -��Ҳ��ΪLoader�������ԣ�ԭʼ��Loader���룬����ͨ���������ε����������������á�"""
    return yml_config

