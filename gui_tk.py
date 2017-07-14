# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Testing-tools
# author: "Lei Yong"
# creation time: 2017/7/12 0012 21:36
# Email: leiyong711@163.com
import re
import os
import time
import Tkinter
import ttk
import tkMessageBox
from Tkinter import *

root = Tkinter.Tk()
root.iconbitmap('hah.ico')
root.title('测试小工具(Last indulge)')
root.geometry('930x730')

canvas = Tkinter.Canvas(root, width=1920, height=1080, bg='#EAEAEA')
canvas.pack()

# 在大窗口下定义一个顶级菜单实例
menubar = Menu(root)

def xp():
    tkMessageBox.askyesno('帮助', '如发现BUG请通过邮件\nleiyong711@163.com\n联系作者')
menubar.add_command(label='帮助',command=xp)



def devices():
    xx = []
    def modified(name):
        # try:
        reu = list(os.popen(name).readlines())
        return re.findall('.*', reu[0])[0]  # ([^\s\\\]+)
        # except:
        #     return u'该机型获取信息异常'
    try:
        brand = modified('adb shell getprop ro.product.brand')  # 读取手机品牌

        phone_models = modified('adb shell getprop ro.semc.product.name')  # 读取设备型号
        deviceVersion = modified('adb shell getprop ro.build.version.release')  # 读取设备系统版本号
        readDeviceId = list(os.popen('adb devices').readlines())  # 读取设备 id
        device = str(readDeviceId[1])[:-8]
        if device == '':
            device = '该机型获取信息异常'
        pp_win.insert(0, brand)
        xh_win.insert(0, phone_models)
        bb_win.insert(0, deviceVersion)
        devices_win.insert(0, device)
    except:
        tkMessageBox.showerror('警告', '请查看设备是否正常连上PC\nUSB调试是否打开')


def ApkInfo(path, name, search):
    aapt = list(os.popen(r'I:\\android-sdk-windows\\build-tools\\18.1.0\\aapt dump badging %s\%s'% (path, name)).readlines())
    if aapt == []:
        return ('请查看路径与包名是否正确')
    else:
        for i in range(0, len(aapt)):  # 遍历列
            a = str(aapt[i])  # 列表转字符串
            sStr2 = search  # 要查询的字符串
            p = a.find(sStr2)  # 判断字符串是否存在，不存在赋值-1
            if p != -1:
                result = aapt[i].split(search)[1:]  # 获取查询参数在列表中的索引截取参数值
                if search == 'launchable-activity: name=':  # 判断是否查询包名
                    result = result[0].split("label=")[:1]  # 如果是查询启动类就截取“label”前的值
                if search == 'package: name=':  # 判断是否查询包名
                    result = result[0].split("versionCode=")[:1]  # 如果是查询包名就截取“versionCode=”前的值
                App_Information = "".join(result).strip('\n').strip("'")  # 去掉字符串中的换行与'号
                return App_Information.strip().lstrip().rstrip("'")  # 去空格及特殊符号并返回查询结果



def aaptx():
    path = path_win.get()
    name = name_win.get()
    if path == '':
        tkMessageBox.showerror('警告', '请填写正确的应用路径')
    elif name == '':
        tkMessageBox.showerror('警告', '请填写正确的应用名')
    else:
        appPackage = ApkInfo(path, name, 'package: name=')  # 获取应用包名
        appb_win.insert(0, appPackage)
        appActivity = ApkInfo(path, name, 'launchable-activity: name=')  # 获取启动类
        appa_win.insert(0, appActivity)



def monkey():
    ti = jg_ac.get()
    packagename = monkeybao_win.get()
    sl = monkeysl_win.get()
    print('包名：%s 随机次数：%s 时间间隔：%s' % (packagename, sl, ti))
    os.popen('adb shell monkey -p %s -s %s -v %s' % (packagename, ti, sl))


def cs(packagename, activity):
    li = os.popen('adb shell am start -W %s/%s' % (packagename, activity)).readlines()
    print(li[-3])

    time.sleep(3)
    os.popen('adb shell am force-stop %s' % packagename)
    time.sleep(1)
    return li[-3]


def qdsj():
    ti = int(ceshu_ac.get())
    packagename = qbao_win.get()
    activity = qActivity_win.get()
    if packagename == '':
        tkMessageBox.showerror('警告', '请填写测试包名')
    elif activity == '':
        tkMessageBox.showerror('警告', '请填写测试包Activity')
    else:
        os.popen('adb shell am force-stop %s' % packagename)
        for i in range(ti):
            qds_win.insert(0, str(cs(packagename, activity)) + 'ms')



#
# c = tkinter.Button(root, text='增加', bg='#B8B8B8', command=helloButton1)
# s = tkinter.Label(root, text='显示', bg='blue')
# button = tkinter.Button(root, text='显示', bg='#B8B8B8', fg='red', command = helloButton)

# 下拉框配置
# 参数次数
num = [50, 100, 150, 200, 300]
cishu_ac = ttk.Combobox(root, values=num, state='readonly', width=5)
cishu_ac.current(0)
# 测试次数
num1 = [1, 3, 5, 10, 15]
ceshu_ac = ttk.Combobox(root, values=num1, state='readonly', width=5)
ceshu_ac.current(0)
# 时间间隔
num2 = [500, 1000, 1500, 2000, 3000]
jg_ac = ttk.Combobox(root, values=num2, state='readonly', width=5)
jg_ac.current(0)

# 按钮文本配置
devicesb = Tkinter.Button(root, text='查询设备信息', bg='#B8B8B8', font=('', 11), command=devices)  # 性能测试‘开始按钮’
app = Tkinter.Button(root, text='查询安装包信息', bg='#B8B8B8', font=('', 11), command=aaptx)  # 性能测试‘开始按钮’
ks = Tkinter.Button(root, text='开始测试', bg='#B8B8B8')  # 性能测试‘开始按钮’
csb = Tkinter.Button(root, text='启动测试', bg='#B8B8B8', command=qdsj)  # 启动时间测试‘开始按钮’
monkeyb = Tkinter.Button(root, text='启动Monkey测试', bg='#B8B8B8', command=monkey)  # Monkey测试‘开始按钮’

# 输入文本配置
path_win = Tkinter.Entry(root, width=30)  # ‘应用路径’输入框
name_win = Tkinter.Entry(root, width=30)  # ‘应用名’输入框
baoi_win = Tkinter.Entry(root, width=30)  # 性能测试‘包名’输入框
qbao_win = Tkinter.Entry(root, width=30)  # 启动测试‘测试包名’输入框
qActivity_win = Tkinter.Entry(root, width=35)  # 启动测试‘包Activity’输入框
monkeybao_win = Tkinter.Entry(root, width=35)  # Mokey测试‘测试包名’输入框
monkeysl_win = Tkinter.Entry(root, width=35)  # Mokey测试‘随机种子数量’输入框

# 输出文本配置
pp_win = Tkinter.Listbox(root, width=30, height=1)  # 品牌输出
xh_win = Tkinter.Listbox(root, width=30, height=1)  # 型号输出
bb_win = Tkinter.Listbox(root, width=30, height=1)  # Android版本输出
devices_win = Tkinter.Listbox(root, width=30, height=1)  # 设备号输出
appb_win = Tkinter.Listbox(root, width=30, height=1)  # 设备号输出
appa_win = Tkinter.Listbox(root, width=30, height=1)  # 设备号输出
cpu_win = Tkinter.Listbox(root, width=30, height=4)  # cpu输出
liul_win = Tkinter.Listbox(root, width=40, height=4)  # 流量输出
ram_win = Tkinter.Listbox(root, width=30, height=4)  # 内存输出
qds_win = Tkinter.Listbox(root, width=30, height=6)  # 内存输出

# 文字控件配置
cx = Tkinter.Label(root, text='信息查询', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
pplabel = Tkinter.Label(root, text='手机品牌：', bg='#EAEAEA')
xhlabel = Tkinter.Label(root, text='型号：', bg='#EAEAEA')
bblabel = Tkinter.Label(root, text='Android版本：', bg='#EAEAEA')
sblabel = Tkinter.Label(root, text='设备号：', bg='#EAEAEA')
pathlabel = Tkinter.Label(root, text='应用路径：', bg='#EAEAEA')
namelabel = Tkinter.Label(root, text='应用名：', bg='#EAEAEA')
appblabel = Tkinter.Label(root, text='应用包名：', bg='#EAEAEA')
appalabel = Tkinter.Label(root, text='启动类名：', bg='#EAEAEA')

qd = Tkinter.Label(root, text='启动时间测试', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
qbaolabel = Tkinter.Label(root, text='测试包名：', bg='#EAEAEA')
qActivitylabel = Tkinter.Label(root, text='测试包Activity：', bg='#EAEAEA')
qnumlabel = Tkinter.Label(root, text='测试次数：', bg='#EAEAEA')
qdslabel = Tkinter.Label(root, text='启动时间展示：', bg='#EAEAEA')
monkeylabel = Tkinter.Label(root, text='Monkey测试', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
monkeybaolabel = Tkinter.Label(root, text='测试包名：', bg='#EAEAEA')
monkeyslabel = Tkinter.Label(root, text='随机种子数量：', bg='#EAEAEA')
monkeytilabel = Tkinter.Label(root, text='时间间隔：', bg='#EAEAEA')

# 下拉框布局

canvas.create_window(895, 265, window=ceshu_ac)  # 性能测试‘测试次数’按钮布局
canvas.create_window(895, 620, window=jg_ac)  # Mokey测试‘时间间隔’按钮布局

# 按钮布局
canvas.create_window(780, 85, window=devicesb)  # 性能测试‘查询设备信息’按钮布局
canvas.create_window(780, 167, window=app)  # 性能测试‘查询设备信息’按钮布局

canvas.create_window(400, 345, window=csb)  # 启动时间‘启动测试’按钮布局
canvas.create_window(400, 670, window=monkeyb)  # Monkey‘启动测试’按钮布局

# 文字控件布局
canvas.create_window(400, 25, window=cx)  # ‘信息查询’文字布局
canvas.create_window(80, 70, window=pplabel)  # 品牌文字布局
canvas.create_window(80, 100, window=xhlabel)  # 型号文字布局
canvas.create_window(410, 70, window=bblabel)  # Android版本文字布局
canvas.create_window(410, 100, window=sblabel)  # 设备号文字布局
canvas.create_window(80, 155, window=pathlabel)  # 应用路径文字布局
canvas.create_window(80, 185, window=namelabel)  # 应用名文字布局
canvas.create_window(410, 155, window=appblabel)  # 包名文字布局
canvas.create_window(410, 185, window=appalabel)  # 启动类号文字布局
canvas.create_window(400, 230, window=qd)  # ‘启动时间测试’文字布局
canvas.create_window(80, 265, window=qbaolabel)  # 启动时间测试‘测试包名’文字布局
canvas.create_window(450, 265, window=qActivitylabel)  # 启动时间测试‘测试包Activity’文字布局
canvas.create_window(830, 265, window=qnumlabel)  # 启动时间测试‘测试次数’文字布局
canvas.create_window(70, 345, window=qdslabel)  # 启动时间测试‘启动时间展示’文字布局
canvas.create_window(400, 430, window=monkeylabel)  # Monkey测试文字布局
canvas.create_window(70, 620, window=monkeybaolabel)  # Monkey测试‘测试包名’文字布局
canvas.create_window(450, 620, window=monkeyslabel)  # Monkey测试‘随机种子数量’文字布局
canvas.create_window(830, 620, window=monkeytilabel)  # Monkey测试‘种子间隔’文字布局

# 输入文本布局
canvas.create_window(230, 155, window=path_win)  # ‘应用路径：’输入文本布局
canvas.create_window(230, 185, window=name_win)  # ‘应用名：’输入文本布局
canvas.create_window(230, 265, window=qbao_win)  # 启动时间测试‘测试包名：’输入文本布局
canvas.create_window(650, 265, window=qActivity_win)  # 启动时间测试‘测试包Activity：’输入文本布局
canvas.create_window(230, 620, window=monkeybao_win)  # Mokey测试‘测试包名：’输入文本布局
canvas.create_window(650, 620, window=monkeysl_win)  # Mokey测试‘随机种子数量：’输入文本布局


# 输出文本布局
canvas.create_window(230, 70, window=pp_win)  # 性能测试‘品牌’输出文本布局
canvas.create_window(230, 100, window=xh_win)  # 性能测试‘型号’输出文本布局
canvas.create_window(580, 70, window=bb_win)  # 性能测试‘’输出文本布局
canvas.create_window(580, 100, window=devices_win)  # 性能测试‘设备号’输出文本布局
canvas.create_window(580, 155, window=appb_win)  # ‘应用包名’输出文本布局
canvas.create_window(580, 185, window=appa_win)  # ‘启动类’输出文本布局

canvas.create_window(230, 344, window=qds_win)  # 启动测试‘启动时间展示’输出文本布局

# 菜单实例应用到大窗口中
root['menu']=menubar

root.mainloop()
