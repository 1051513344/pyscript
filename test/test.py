#coding=gbk
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
response_html = requests.get("https://www.usgbc.org/projects?Country=%5B%22China%22%5D").content.decode("utf-8")
with open("response_html.html", "w", encoding='utf-8') as f:
    f.write(response_html)
