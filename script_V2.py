#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32gui, win32api, win32con
from PIL import ImageGrab, Image, ImageDraw
import cv2
import time, random
from ctypes import *
from ctypes.wintypes import *

gdi32 = windll.gdi32
user32 = windll.user32

classname = 'Qt5QWindowIcon'
titlename = '夜神模拟器'
#获取模拟器窗口句柄（尺寸）
hwnd = win32gui.FindWindow(classname, titlename)
try:
    f = ctypes.windll.dwmapi.DwmGetWindowAttribute
except WindowsError:
    f = None
if f:
    rect = ctypes.wintypes.RECT()
    DWMWA_EXTENDED_FRAME_BOUNDS = 9
    f(ctypes.wintypes.HWND(hwnd),
      ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
      ctypes.byref(rect),
      ctypes.sizeof(rect)
      )
    size = (rect.right, rect.left, rect.bottom, rect.top)

#截图模块
def screenshot():
    bbox = (rect.left, rect.top, rect.right, rect.bottom)
    im = ImageGrab.grab(bbox)
    im.save('sc.png')
    img = cv2.imread('D:\pycharm\YYS_Script\Onmyouji_Script\sc.png', 0)
    return img #指代截图

#准备模块，设置刷御魂次数模块
def begin():
    start = cv2.imread('D:\pycharm\YYS_Script\Onmyouji_Script\start.png', 0)
    end = cv2.imread('D:\pycharm\YYS_Script\Onmyouji_Script\share.png', 0)
    n = input("请输入刷御魂次数：")
    n = int(n)
    return start, end, n

#匹配模块,检测，点击屏幕上的“挑战”
def matchT(t, x, y):
    sd = 0
    while sd < 15:
        img1 = screenshot()  #目标图像-屏幕截图（有读图操作）
        res = match(img1, t) #将屏幕截图和自备图进行比较
        threshold = 0.70 #设定阈值
        if res > threshold: #如果threshold大于0.7
            break
        else:
            get_randtime(0.5, 1)
        sd += 1
        sx, sy = get_randxy(x, y)
        get_randtime(0.02, 0.03)
        click(sx, sy) #进行点击
        get_randtime(0.02, 0.05)

#产生随机时间延迟
def get_randtime(a, b):
    time.sleep(random.uniform(a, b))

#点击模块。输入两个二维列表，表示要点击的位置的x坐标，y坐标
def click(x, y):
    win32api.SetCursorPos((int(0.81*x), int(0.81*y)))    # 鼠标定位到坐标(x, y)。注意：不同的屏幕分辨率会影响到鼠标的定位，有需求的请用百分比换算
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)    # 鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 鼠标左键弹起

#获取随机XY，产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围
def get_randxy(x, y):
    xc = random.randint(int(x[0]), int(x[1]))
    yc = random.randint(int(y[0]), int(y[1]))
    return xc,yc

#图像匹配模块，img1代表待匹配图像-屏幕刚刚截图的图像, template代表模板-我们已经有的自备图像。确保img1和temp都已经进行读图、灰度化操作
def match(img1, template):
    res = cv2.matchTemplate(img1, template, cv2.TM_CCOEFF_NORMED) #计算归一化相关系数，越接近1越相关
    maxres = res.max()
    return maxres

#开始战斗后等待一段时间后，点击三下跳过结算动画界面
def endclick(end_x, end_y):
    get_randtime(15, 19)
    for i in range(1, 4):
        ex, ey = get_randxy(end_x, end_y)
        click(ex, ey)
        get_randtime(0.8, 1.5)

def main():
    print('痒痒鼠小助手 V2.0 启动！')
    start, end, n = begin() #自备的模板图像已经进行读图、灰度化操作
    #开始刷御魂点击范围
    start_x = [rect.right*0.89, rect.right*0.9]  #用一个列表存储X范围。它们乘上的系数是个人亲手按比例算的……
    start_y = [rect.bottom*0.89, rect.bottom*0.9]
    #print(start_x, start_y) #[613.21, 620.1] [453.01, 458.1]

    #刷御魂结束时，点击范围
    end_x = [rect.left*11, rect.left*17.8]
    end_y = [rect.top*3, rect.top*3.5]
    for k in range(n): #n为御魂次数
        print('开始进行第{}局魂十'.format(k + 1))
        matchT(start, start_x, start_y)
        endclick(end_x, end_y)
        matchT(end, end_x, end_y)
    print('进行了{}次魂十'.format(n))

if __name__ == '__main__':
    main()
