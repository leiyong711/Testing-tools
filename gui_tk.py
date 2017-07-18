# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: adb
# author: "Lei Yong"
# creation time: 2017/7/14 0014 18:28
# Email: leiyong711@163.com

import os
import time
import Tkinter
import ttk
import tkMessageBox
from Tkinter import *


def lei(version):
    root = Tkinter.Tk()
    root.iconbitmap('logo.ico')
    root.title('测试小工具(Last indulge)')
    root.geometry('930x680')

    canvas = Tkinter.Canvas(root, width=1920, height=1080, bg='#EAEAEA')
    canvas.pack()

    # 在大窗口下定义一个顶级菜单实例
    menubar = Menu(root)

    def xp():
        tkMessageBox.askyesno('帮助', '如发现BUG请通过邮件\nleiyong711@163.com\n联系作者。\n\n\n     当前版本 %s'
                              % version)
    menubar.add_command(label='帮助', command=xp)

    def devices():
        def modified(name):
            reu = list(os.popen(name).readlines())
            return re.findall('.*', reu[0])[0]  # ([^\s\\\]+)
        try:
            brand = modified('adb shell getprop ro.product.brand')  # 读取手机品牌
            phone_models = modified('adb shell getprop ro.semc.product.name')  # 读取设备型号
            deviceversion = modified('adb shell getprop ro.build.version.release')  # 读取设备系统版本号
            read_deviceid = list(os.popen('adb devices').readlines())  # 读取设备 id
            device = str(read_deviceid[1])[:-8]
            if device == '':
                device = '该机型获取信息异常'
            pp_win.insert(0, brand)
            xh_win.insert(0, phone_models)
            bb_win.insert(0, deviceversion)
            devices_win.insert(0, device)
        except:
            tkMessageBox.showerror('警告', '请查看设备是否正常连上PC\nUSB调试是否打开')

    def ApkInfo(path, name, search):
        t = os.popen('cd').read()
        aapt = list(os.popen('%s: &aapt dump badging %s\\%s'
                             % (t[0], path, name)).readlines())
        if aapt == ['']:
            return '请查看路径与包名是否正确'
        else:
            for i in range(0, len(aapt)):  # 遍历列
                a = str(aapt[i])  # 列表转字符串
                sstr2 = search  # 要查询的字符串
                p = a.find(sstr2)  # 判断字符串是否存在，不存在赋值-1
                if p != -1:
                    result = aapt[i].split(search)[1:]  # 获取查询参数在列表中的索引截取参数值
                    if search == 'launchable-activity: name=':  # 判断是否查询包名
                        result = result[0].split("label=")[:1]  # 如果是查询启动类就截取“label”前的值
                    if search == 'package: name=':  # 判断是否查询包名
                        result = result[0].split("versionCode=")[:1]  # 如果是查询包名就截取“versionCode=”前的值
                    app_information = "".join(result).strip('\n').strip("'")  # 去掉字符串中的换行与'号
                    return app_information.strip().lstrip().rstrip("'")  # 去空格及特殊符号并返回查询结果

    def aaptx():
        path = path_win.get()
        name = name_win.get()
        if path == '':
            tkMessageBox.showerror('警告', '请填写正确的应用路径')
        elif name == '':
            tkMessageBox.showerror('警告', '请填写正确的应用名')
        else:
            apppackage = ApkInfo(path, name, 'package: name=')  # 获取应用包名
            appb_win.insert(0, apppackage)
            appactivity = ApkInfo(path, name, 'launchable-activity: name=')  # 获取启动类
            appa_win.insert(0, appactivity)

    def monkey():
        packagename = monkeybao_win.get()
        zhongzi = monkeysl_win.get()
        cishu = jg_ac.get()
        daohang = mkdaohang_win.get()
        chumo = mkchumo_win.get()
        huadong = mkhuadong_win.get()
        guiji = mkguiji_win.get()
        xiton = mkxitongb_win.get()
        aqiehuan = mkactivity_win.get()
        shijinaliang = mkshijian_win.get()
        log = mklog_win.get()
        path = os.path.isdir(log)
        k = [daohang, chumo, huadong, guiji, xiton, aqiehuan]
        for i in range(len(k)):
            if k[i] != '':
                continue
            else:
                k[i] = 0
        tie = time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))
        if packagename == '':
            tkMessageBox.showerror('警告', '请填写测试包名')
        elif zhongzi == '':
            tkMessageBox.showerror('警告', '请填写随机种子数量')
        elif shijinaliang == '':
            tkMessageBox.showerror('警告', '请填写事件量')
        elif log == '':
            tkMessageBox.showerror('警告', '请填写日志存放路径')
        elif path == False:
            tkMessageBox.showerror('警告', '日志路径不正确\n请填写正确的日志存放路径')

        # '包，种子，时间，忽略程序崩溃 、 忽略超时 、 监视本地程序崩溃 、 详细信息级别为2,导航事件，触摸事件，滑动，
        # 轨迹球事件，系统按键，act切换,事件量 日志'
        else:
            os.popen('mkdir %s\\%s' % (log, tie))
            num = 'adb shell monkey -p %s -s %s --ignore-crashes --ignore-timeouts --monitor-native-crashes ' \
                  '--throttle %s --pct-nav %s --pct-touch %s --pct-motion %s --pct-trackball %s --pct-syskeys %s ' \
                  '--pct-appswitch %s -v -v %s > %s\\%s\\hmonkeylog.txt' % (packagename, zhongzi, cishu, k[0],
                                                                            k[1], k[2], k[3], k[4], k[5],
                                                                            shijinaliang, log, tie)
            print path
            os.popen(num)
            print log + tie + r'\hmonkeylog.txt'
            pd = os.path.exists(log + '\\' + tie + '\\hmonkeylog.txt')
            if pd == True:
                tkMessageBox.showinfo('导出monkey日志', '日志成功导出\n\n请到 %s\\%s\\ 路径下\n查看 hmonkeylog.txt '
                                                        '日志文件'% (log, tie))
            else:
                tkMessageBox.showerror('导出monkey日志', '日志导出失败')

    def cs(packagename, activity):
        li = os.popen('adb shell am start -W %s/%s' % (packagename, activity)).readlines()
        time.sleep(3)
        os.popen('adb shell am force-stop %s' % packagename)
        time.sleep(1)
        return li[-3]

    def qdsj():
        ti = int(ceshu_ac.get())
        packagename = qbao_win.get()
        activity = qactivity_win.get()
        if packagename == '':
            tkMessageBox.showerror('警告', '请填写测试包名')
        elif activity == '':
            tkMessageBox.showerror('警告', '请填写测试包Activity')
        else:
            os.popen('adb shell am force-stop %s' % packagename)
            for i in range(ti):
                qds_win.insert(0, str(cs(packagename, activity)) + 'ms')

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
    # 性能测试‘开始按钮’
    devicesb = Tkinter.Button(root, text='查询设备信息', bg='#B8B8B8', font=('', 11), command=devices)
    # 性能测试‘开始按钮’
    app = Tkinter.Button(root, text='查询安装包信息', bg='#B8B8B8', font=('', 11), command=aaptx)
    csb = Tkinter.Button(root, text='启动测试', bg='#B8B8B8', command=qdsj)  # 启动时间测试‘开始按钮’
    monkeyb = Tkinter.Button(root, text='启动Monkey测试', bg='#B8B8B8', command=monkey)  # Monkey测试‘开始按钮’

    # 输入文本配置
    path_win = Tkinter.Entry(root, width=30)  # ‘应用路径’输入框
    name_win = Tkinter.Entry(root, width=30)  # ‘应用名’输入框
    qbao_win = Tkinter.Entry(root, width=30)  # 启动测试‘测试包名’输入框
    qactivity_win = Tkinter.Entry(root, width=30)  # 启动测试‘包Activity’输入框
    monkeybao_win = Tkinter.Entry(root, width=30)  # Mokey测试‘测试包名’输入框
    monkeysl_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mkdaohang_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mkchumo_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mkhuadong_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mkguiji_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mkxitongb_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mkactivity_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mkshijian_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框
    mklog_win = Tkinter.Entry(root, width=30)  # Mokey测试‘随机种子数量’输入框

    # 输出文本配置
    pp_win = Tkinter.Listbox(root, width=30, height=1)  # 品牌输出
    xh_win = Tkinter.Listbox(root, width=30, height=1)  # 型号输出
    bb_win = Tkinter.Listbox(root, width=30, height=1)  # Android版本输出
    devices_win = Tkinter.Listbox(root, width=30, height=1)  # 设备号输出
    appb_win = Tkinter.Listbox(root, width=30, height=1)  # 设备号输出
    appa_win = Tkinter.Listbox(root, width=30, height=1)  # 设备号输出
    qds_win = Tkinter.Listbox(root, width=30, height=6)  # 内存输出

    # 文字控件配置
    banbenlabel = Tkinter.Label(root, text='版本 %s' % version, bg='#EAEAEA', fg='red', font=("黑体", 12, "bold"))
    cx = Tkinter.Label(root, text='信息查询', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
    pplabel = Tkinter.Label(root, text='手机品牌：', bg='#EAEAEA')
    xhlabel = Tkinter.Label(root, text='型号：', bg='#EAEAEA')
    bblabel = Tkinter.Label(root, text='Android版本：', bg='#EAEAEA')
    sblabel = Tkinter.Label(root, text='设备号：', bg='#EAEAEA')
    pathlabel = Tkinter.Label(root, text='应用路径：', bg='#EAEAEA')
    namelabel = Tkinter.Label(root, text='应用名：', bg='#EAEAEA')
    appblabel = Tkinter.Label(root, text='应用包名：', bg='#EAEAEA')
    appalabel = Tkinter.Label(root, text='启动类名：', bg='#EAEAEA')
    qd = Tkinter.Label(root, text='启动时间测试', bg='#EAEAEA', fg='red', font=21)
    qbaolabel = Tkinter.Label(root, text='测试包名：', bg='#EAEAEA')
    qactivitylabel = Tkinter.Label(root, text='测试包Activity：', bg='#EAEAEA')
    qnumlabel = Tkinter.Label(root, text='测试次数：', bg='#EAEAEA')
    qdslabel = Tkinter.Label(root, text='启动时间展示：', bg='#EAEAEA')
    monkeylabel = Tkinter.Label(root, text='Monkey测试', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
    monkeybaolabel = Tkinter.Label(root, text='测试包名：', bg='#EAEAEA')
    monkeyslabel = Tkinter.Label(root, text='随机种子数量：', bg='#EAEAEA')
    monkeytilabel = Tkinter.Label(root, text='时间间隔：', bg='#EAEAEA')
    mkdaohanglabel = Tkinter.Label(root, text='导航事件百分比：', bg='#EAEAEA')
    mkchumolabel = Tkinter.Label(root, text='触摸事件百分比：', bg='#EAEAEA')
    mkhuadonglabel = Tkinter.Label(root, text='滑动事件百分比：', bg='#EAEAEA')
    mkguijiqlabel = Tkinter.Label(root, text='轨迹球事件百分比：', bg='#EAEAEA')
    mkanjianlabel = Tkinter.Label(root, text='系统按键百分比：', bg='#EAEAEA')
    mkactivitylabel = Tkinter.Label(root, text='Activity之间切换百分比：', bg='#EAEAEA')
    mksjllabel = Tkinter.Label(root, text='事件量：', bg='#EAEAEA')
    mkloglabel = Tkinter.Label(root, text='日志存放路径：', bg='#EAEAEA')

    # 下拉框布局
    canvas.create_window(895, 265, window=ceshu_ac)  # 性能测试‘测试次数’按钮布局
    canvas.create_window(895, 460, window=jg_ac)  # Mokey测试‘时间间隔’按钮布局

    # 按钮布局
    canvas.create_window(780, 85, window=devicesb)  # 性能测试‘查询设备信息’按钮布局
    canvas.create_window(780, 167, window=app)  # 性能测试‘查询设备信息’按钮布局
    canvas.create_window(400, 345, window=csb)  # 启动时间‘启动测试’按钮布局
    canvas.create_window(400, 620, window=monkeyb)  # Monkey‘启动测试’按钮布局

    # 文字控件布局
    canvas.create_window(850, 30, window=banbenlabel)  # ‘信息查询’文字布局
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
    canvas.create_window(450, 265, window=qactivitylabel)  # 启动时间测试‘测试包Activity’文字布局
    canvas.create_window(830, 265, window=qnumlabel)  # 启动时间测试‘测试次数’文字布局
    canvas.create_window(70, 345, window=qdslabel)  # 启动时间测试‘启动时间展示’文字布局
    canvas.create_window(400, 420, window=monkeylabel)  # Monkey测试文字布局
    canvas.create_window(80, 460, window=monkeybaolabel)  # Monkey测试‘测试包名’文字布局
    canvas.create_window(450, 460, window=monkeyslabel)  # Monkey测试‘随机种子数量’文字布局
    canvas.create_window(830, 460, window=monkeytilabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(62, 490, window=mkdaohanglabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(444, 490, window=mkchumolabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(62, 520, window=mkhuadonglabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(438, 520, window=mkguijiqlabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(62, 550, window=mkanjianlabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(424, 550, window=mkactivitylabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(87, 580, window=mksjllabel)  # Monkey测试‘种子间隔’文字布局
    canvas.create_window(450, 580, window=mkloglabel)  # Monkey测试‘种子间隔’文字布局

    # 输入文本布局
    canvas.create_window(230, 155, window=path_win)  # ‘应用路径：’输入文本布局
    canvas.create_window(230, 185, window=name_win)  # ‘应用名：’输入文本布局
    canvas.create_window(230, 265, window=qbao_win)  # 启动时间测试‘测试包名：’输入文本布局
    canvas.create_window(610, 265, window=qactivity_win)  # 启动时间测试‘测试包Activity：’输入文本布局
    canvas.create_window(230, 460, window=monkeybao_win)  # Mokey测试‘测试包名：’输入文本布局
    canvas.create_window(610, 460, window=monkeysl_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(230, 490, window=mkdaohang_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(610, 490, window=mkchumo_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(230, 520, window=mkhuadong_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(610, 520, window=mkguiji_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(230, 550, window=mkxitongb_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(610, 550, window=mkactivity_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(230, 580, window=mkshijian_win)  # Mokey测试‘随机种子数量：’输入文本布局
    canvas.create_window(610, 580, window=mklog_win)  # Mokey测试‘随机种子数量：’输入文本布局

    # 输出文本布局
    canvas.create_window(230, 70, window=pp_win)  # 性能测试‘品牌’输出文本布局
    canvas.create_window(230, 100, window=xh_win)  # 性能测试‘型号’输出文本布局
    canvas.create_window(580, 70, window=bb_win)  # 性能测试‘’输出文本布局
    canvas.create_window(580, 100, window=devices_win)  # 性能测试‘设备号’输出文本布局
    canvas.create_window(580, 155, window=appb_win)  # ‘应用包名’输出文本布局
    canvas.create_window(580, 185, window=appa_win)  # ‘启动类’输出文本布局
    canvas.create_window(230, 344, window=qds_win)  # 启动测试‘启动时间展示’输出文本布局

    # 菜单实例应用到大窗口中
    root['menu'] = menubar
    root.mainloop()


def sj(win, info):
    root = Tkinter.Tk()
    root.iconbitmap('logo.ico')
    root.title('测试小工具(Last indulge)')
    root.geometry('930x730')
    tkMessageBox.showinfo(win, info)


def error(win, info):
    root = Tkinter.Tk()
    root.iconbitmap('logo.ico')
    root.title('测试小工具(Last indulge)')
    root.geometry('930x730')
    tkMessageBox.showerror(win, info)
