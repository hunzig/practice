import pyautogui
import random
import time
pyautogui.FAILSAFE =True
		
time.sleep(2)


def  submitJingying():
	i = 1
	while i < 11:
		#点击我要报送
		pyautogui.moveTo(116,358,duration=0.25)
		pyautogui.click()
		#点击地址栏
		pyautogui.moveTo(465,345,duration=0.25)
		pyautogui.click()
		#输入网址加随机值
		randomNumber = random.randint(100000000,999999999)
		pyautogui.typewrite("http://dongyang.ga:7373/index.html?=i" + str(randomNumber))
		#选择回帖
		pyautogui.moveTo(535,522,duration=0.25)
		pyautogui.click()
		#选择经营
		pyautogui.moveTo(520,586,duration=0.25)
		pyautogui.click()
		#提交报送
		pyautogui.moveTo(937,666,duration=0.25)
		pyautogui.click()
		time.sleep(1)
		#继续报送
		pyautogui.moveTo(494,451,duration=0.25)
		time.sleep(1)
		i += 1

def submitXuanchuan():	
	i = 1
	while i < 11 :
		#点击我要报送
		pyautogui.moveTo(116,358,duration=0.25)
		pyautogui.click()
		#点击地址栏
		pyautogui.moveTo(465,345,duration=0.25)
		pyautogui.click()
		#输入网址加随机值
		randomNumber = random.randint(100000000,999999999)
		pyautogui.typewrite("http://dongyang.ga:7373/index.html?=i" + str(randomNumber))
		#选择主帖
		pyautogui.moveTo(467,522,duration=0.25)
		pyautogui.click()
		#选择宣传
		pyautogui.moveTo(571,586,duration=0.25)
		pyautogui.click()
		#提交报送
		pyautogui.moveTo(937,666,duration=0.25)
		pyautogui.click()
		time.sleep(1)
		#继续报送
		pyautogui.moveTo(494,451,duration=0.25)
		time.sleep(1)
		i += 1



i = 1
while i < 6 :

	
	#选择身份栏
	pyautogui.moveTo(847,458,duration=0.25)
	pyautogui.click()
	#选择身份
	pyautogui.press(['down'])
	pyautogui.press('enter')
	#点击确定
	pyautogui.click()
	time.sleep(1)
	#开始填写表单并提交
	submitJingying()

	#提交后停顿片刻
	time.sleep(1)
	i += 1


submitXuanchuan()
