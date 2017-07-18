# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: adb
# author: "Lei Yong" 
# creation time: 2017/7/14 0014 18:28
# Email: leiyong711@163.com

import urllib
import json
import gui_tk

url2 = 'http://orangep.cn:9998/adbinfo.txt'
version = '1.1'
banben = u'\n\n当前版本 %s' % version


def ks():
    try:
        http = urllib.urlopen(url2).read()
        https = http#.decode('gbk')
        return json.loads(https)
    except:
        return '服务器错误'

k = 0
b = ks()
if b == '服务器错误':
    k = 9
    gui_tk.sj('异常', '连接服务器异常\r\n\n解决方法：\r\n  '
                   '1.请查看当前网络是否正常\n  '
                   '2.此应用是否被360类软件禁网\n  '
                   '3.如若无法解决请通过邮件联系作者\n  leiyong711@163.com')

elif b['state'].encode('utf-8') == '正常':
    for i in range(len(b["version"])):
        if b["version"][i].encode('utf-8') == version:
            gui_tk.lei(version)
            k = 1
if k == 0:
    gui_tk.sj(b['error']['win'], b['error']['info']+banben)
