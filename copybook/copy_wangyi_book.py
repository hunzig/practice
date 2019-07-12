# 该代码理论上可行，但是执行中途会出错，网易可能有校验机制，短时间快速翻页会终止


import pyautogui
import time

#睡5秒钟，同时打开书本
time.sleep(5)

#设定一个页码范围
for i in range(1000):
    #翻页
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    time.sleep(2)
    #保存截图
    pyautogui.screenshot('./images/page_%d.jpg'%i)
    
    time.sleep(3)
