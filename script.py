#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pyautogui
import time, datetime
import random
import os, sys

def locate():
    '''在当前屏幕找到相应的像素，匹配像素的颜色，确定为“挑战”按钮。'''
    start = pyautogui.pixelMatchesColor(852, 995, (229, 220, 196))
    if start:
        print(datetime.datetime.now().strftime('%F %T'), "魂十 匹配成功")
        pyautogui.moveTo(random.randint(813, 881),random.randint(929, 1006))
        pyautogui.click()

def ifEqual():
    '''战斗结束时，结算界面对达摩操作'''
    #global TTL
    ifEqual100 = pyautogui.pixelMatchesColor(671, 621, ( 231, 214, 170 )) #出现达摩
    if ifEqual100:
        print(datetime.datetime.now().strftime('%F %T'), "结束挑战")
        time.sleep(random.uniform(0.05, 0.15))
        for i in range(0, random.randint(13, 16)):#设置鼠标点击次数5~8次
            pyautogui.moveTo(random.randint(237, 485), random.randint(521, 589))
            time.sleep(random.uniform(0.05, 0.10))
            pyautogui.click()
            time.sleep(random.uniform(0.05, 0.10))
    time.sleep(0.1)

if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    print(datetime.datetime.now().strftime('%F %T'))
    print('阴阳师Script V1.0')
    while(True):
        locate()
        ifEqual()
        time.sleep(random.uniform(0.3, 0.5))

'''PyAutoGUI提供了一个保护措施。当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，
PyAutoGUI函数就会产生pyautogui.FailSafeException异常,用于在程序失控时退出'''
