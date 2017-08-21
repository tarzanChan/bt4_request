# -*- coding: utf-8 -*-
__author__ = 'duohappy'
# 导入tkinter包
import Tkinter as tk
# 导入相关爬虫函数
from wochu_price import get_wochu_price
from yiguo_price import get_yiguo_price
root = tk.Tk()  # 建立主窗体
root.title('Have Fun')  # 设置窗体标题
root.geometry('600x200')  # 设置窗口大小
root.resizable(width=True, height=True)  # 窗口是可变大小的
frame_top = tk.Frame(root)  # 在主窗体上建立一个frame
frame_mid = tk.Frame(root)
frame_bottom = tk.Frame(root)
frame_top.pack()  # 显示出frame
frame_mid.pack()
frame_bottom.pack()
tk.Label(frame_top, text='美国红蛇果').pack()  # 建立label并显示出来
tk.Label(frame_mid, text='我厨').grid(row=0, pady=10)  # 上面使用pack
tk.Label(frame_mid, text='易果生鲜').grid(row=1, pady=10)  # 现在使用grid，目的是为了布局更加方便
wochu_price_var = tk.StringVar()  # 创建价格变量
wochu_title_var = tk.StringVar()  # 创建标题变量
wochu_price_entry = tk.Entry(frame_mid, textvariable=wochu_price_var, width=6)  # 创建一个显示条
wochu_title_entry = tk.Entry(frame_mid, textvariable=wochu_title_var, width=50)
wochu_price_entry.grid(row=0, column=1, padx=10)  # 进行布局
wochu_title_entry.grid(row=0, column=2, padx=10)
yiguo_price_var = tk.StringVar()
yiguo_title_var = tk.StringVar()
yiguo_price_entry = tk.Entry(frame_mid, textvariable=yiguo_price_var, width=6)
yiguo_title_entry = tk.Entry(frame_mid, textvariable=yiguo_title_var, width=50)
yiguo_price_entry.grid(row=1, column=1)
yiguo_title_entry.grid(row=1, column=2)
def spider_price():
    wochu_url = 'http://www.wochu.cn/Product/Deatail/349adbd3-9b10-4b60-97d9-fec13c9a56e5'
    yiguo_url = 'http://www.yiguo.com/product/1294029.html'
    wochu_title, wochu_price = get_wochu_price(wochu_url)  # 拆包
    yiguo_title, yiguo_price = get_yiguo_price(yiguo_url)
    wochu_title_var.set(wochu_title)
    wochu_price_var.set(wochu_price)
    yiguo_title_var.set(yiguo_title)
    yiguo_price_var.set(yiguo_price)
tk.Button(frame_bottom, text='spider',
          command=spider_price, padx=10, pady=10).pack()  # 按钮上绑定了一个函数，点击按钮执行spider_price函数
root.mainloop()  # 窗体循环