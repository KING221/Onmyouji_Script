#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pyautogui
import time, datetime
import random

def locate(count):
    '''在当前屏幕找到相应的像素，匹配像素的颜色，确定为“挑战”按钮。'''
    start = pyautogui.locateCenterOnScreen('start04.png', grayscale=False)
    if start:
        print(datetime.datetime.now().strftime('%F %T'), '魂十 匹配成功')
        pyautogui.moveTo(random.randint(start[0]-30, start[0]+30),random.randint(start[1]-30, start[1]+30))
        pyautogui.click()

def ifEqual():
    '''战斗结束时，结算界面对达摩操作'''
    vic = pyautogui.pixelMatchesColor(572, 371, (255, 255, 255))
    if vic:
        print(datetime.datetime.now().strftime('%F %T'), '挖矿结束')
        time.sleep(random.uniform(0.05, 0.15))
        for i in range(0, random.randint(13, 16)):#设置鼠标点击次数5~8次
            pyautogui.moveTo(random.randint(530, 590), random.randint(440, 490))
            time.sleep(random.uniform(0.05, 0.10))
            pyautogui.click()
            time.sleep(random.uniform(0.05, 0.10))
        time.sleep(0.1)

if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    print(datetime.datetime.now().strftime('%F %T'))
    print('阴阳师Script V1.0')
    count = 0
    while(True):
        locate(count)
        ifEqual()
        time.sleep(random.uniform(0.3, 0.5))
        count += 1

'''PyAutoGUI提供了一个保护措施。当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，
PyAutoGUI函数就会产生pyautogui.FailSafeException异常,用于在程序失控时退出'''
