# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Testing-tools
# author: "Lei Yong" 
# creation time: 2017/7/12 0012 21:36
# Email: leiyong711@163.com

import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.iconbitmap('hah.ico')
root.title('测试小工具(Last indulge)')
root.geometry('930x690')

canvas = tkinter.Canvas(root, width=1920, height=1080, bg='#EAEAEA')
canvas.pack()

li = ['0']
s = 0


def helloButton():
    pass


def monkey():
    pass
##
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
num1 = [10, 20, 30, 50, 100]
ceshu_ac = ttk.Combobox(root, values=num1, state='readonly', width=5)
ceshu_ac.current(0)
# 时间间隔
num2 = [500, 1000, 1500, 2000, 3000]
jg_ac = ttk.Combobox(root, values=num2, state='readonly', width=5)
jg_ac.current(0)

# 按钮文本配置
ks = tkinter.Button(root, text='开始测试', bg='#B8B8B8')  # 性能测试‘开始按钮’
csb = tkinter.Button(root, text='启动测试', bg='#B8B8B8')  # 启动时间测试‘开始按钮’
monkeyb = tkinter.Button(root, text='启动Monkey测试', bg='#B8B8B8', command=monkey)  # Monkey测试‘开始按钮’

# 输入文本配置
baoi_win = tkinter.Entry(root, width=30)  # 性能测试‘包名’输入框
qbao_win = tkinter.Entry(root, width=30)  # 启动测试‘包名’输入框
qActivity_win = tkinter.Entry(root, width=35)  # 启动测试‘包Activity’输入框
monkeybao_win = tkinter.Entry(root, width=35)  # Mokey测试‘测试包名’输入框
monkeysl_win = tkinter.Entry(root, width=35)  # Mokey测试‘随机种子数量’输入框

# 输出文本配置
cpu_win = tkinter.Listbox(root, width=30, height=4)  # cpu输出
liul_win = tkinter.Listbox(root, width=40, height=4)  # 流量输出
ram_win = tkinter.Listbox(root, width=30, height=4)  # 内存输出
qds_win = tkinter.Listbox(root, width=30, height=6)  # 内存输出

# 文字控件配置
xn = tkinter.Label(root, text='性能参数展示', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
cpulabel = tkinter.Label(root, text='cpu', bg='#EAEAEA')
liullabel = tkinter.Label(root, text='流量', bg='#EAEAEA')
cs_label = tkinter.Label(root, text='参数次数：', bg='#EAEAEA')
ramlabel = tkinter.Label(root, text='内存', bg='#EAEAEA')
baolabel = tkinter.Label(root, text='包名：', bg='#EAEAEA')
qd = tkinter.Label(root, text='启动时间测试', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
qbaolabel = tkinter.Label(root, text='测试包名：', bg='#EAEAEA')
qActivitylabel = tkinter.Label(root, text='测试包Activity：', bg='#EAEAEA')
qnumlabel = tkinter.Label(root, text='测试次数：', bg='#EAEAEA')
qdslabel = tkinter.Label(root, text='启动时间展示：', bg='#EAEAEA')
monkeylabel = tkinter.Label(root, text='Monkey测试', bg='#EAEAEA', fg='red', font=("黑体", 21, "bold"))
monkeybaolabel = tkinter.Label(root, text='测试包名：', bg='#EAEAEA')
monkeyslabel = tkinter.Label(root, text='随机种子数量：', bg='#EAEAEA')
monkeytilabel = tkinter.Label(root, text='时间间隔：', bg='#EAEAEA')

# 下拉框布局
canvas.create_window(890, 80, window=cishu_ac)  # 性能测试‘参数次数’按钮布局
canvas.create_window(890, 340, window=ceshu_ac)  # 性能测试‘测试次数’按钮布局
canvas.create_window(890, 560, window=jg_ac)  # Mokey测试‘时间间隔’按钮布局

# 按钮布局
canvas.create_window(400, 270, window=ks)  # 性能测试‘开始测试’按钮布局
canvas.create_window(400, 440, window=csb)  # 启动时间‘启动测试’按钮布局
canvas.create_window(400, 670, window=monkeyb)  # Monkey‘启动测试’按钮布局

# 文字控件布局
canvas.create_window(400, 20, window=xn)  # 性能测试文字布局
canvas.create_window(230, 130, window=cpulabel)  # 性能测试‘cpu’文字布局
canvas.create_window(635, 130, window=liullabel)  # 性能测试‘流量’文字布局
canvas.create_window(830, 80, window=cs_label)  # 性能测试‘参数次数’文字布局
canvas.create_window(230, 230, window=ramlabel)  # 性能测试‘内存’文字布局
canvas.create_window(80, 270, window=baolabel)  # 性能测试‘包名：’文字布局
canvas.create_window(400, 310, window=qd)  # ‘启动时间测试’文字布局
canvas.create_window(80, 340, window=qbaolabel)  # 启动时间测试‘测试包名’文字布局
canvas.create_window(450, 340, window=qActivitylabel)  # 启动时间测试‘测试包Activity’文字布局
canvas.create_window(830, 340, window=qnumlabel)  # 启动时间测试‘测试次数’文字布局
canvas.create_window(70, 440, window=qdslabel)  # 启动时间测试‘启动时间展示’文字布局
canvas.create_window(400, 520, window=monkeylabel)  # Monkey测试文字布局
canvas.create_window(80, 560, window=monkeybaolabel)  # Monkey测试‘测试包名’文字布局
canvas.create_window(450, 560, window=monkeyslabel)  # Monkey测试‘随机种子数量’文字布局
canvas.create_window(830, 560, window=monkeytilabel)  # Monkey测试‘种子间隔’文字布局

# 输入文本布局
canvas.create_window(230, 270, window=baoi_win)  # 性能测试‘包名：’输入文本布局
canvas.create_window(230, 340, window=qbao_win)  # 启动时间测试‘测试包名：’输入文本布局
canvas.create_window(650, 340, window=qActivity_win)  # 启动时间测试‘测试包Activity：’输入文本布局
canvas.create_window(230, 560, window=monkeybao_win)  # Mokey测试‘测试包名：’输入文本布局
canvas.create_window(650, 560, window=monkeysl_win)  # Mokey测试‘随机种子数量：’输入文本布局


# 输出文本布局
canvas.create_window(230, 80, window=cpu_win)  # 性能测试‘cpu’输出文本布局
canvas.create_window(635, 80, window=liul_win)  # 性能测试‘流量’输出文本布局
canvas.create_window(230, 180, window=ram_win)  # 性能测试‘内存’输出文本布局
canvas.create_window(230, 440, window=qds_win)  # 性能测试‘内存’输出文本布局

root.mainloop()
