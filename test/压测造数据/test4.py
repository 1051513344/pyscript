
# 评教评学统计的全部页面数据加载

import random

import radar
import requests
import json
import datetime

with open("domain", 'r') as f:
    domain = f.read()
with open("sessionid", 'r') as f:
    sessionid = f.read()



