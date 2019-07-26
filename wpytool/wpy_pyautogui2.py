#代码实现的目的是五个id，每个id提交十个经营类url，外加任意一个id提交十个宣传类id。
#因为url校验机制很弱，所以可以实现全自动完成。
#校验机制为，页面上有id名称即视为发帖有效，故自己制作一个包含五个id的页面即可。
#校验机制二，每个页面url不能重复，所以在每个url后面随机加上一个9位的随机数
#分辨率设置成1920×1080（不然像素点需要重新设置）


import pyautogui
import random
import time
pyautogui.FAILSAFE =True
		
time.sleep(2)

#定义一个经营类提交函数
def  submitJingying():
	for i in range(11):
		#点击我要报送
		pyautogui.click(53,354,duration=0.25)
		#点击地址栏
		pyautogui.click(413,345,duration=0.25)
		#输入网址加随机值
		randomNumber = random.randint(100000000,999999999)
		pyautogui.typewrite("http://dongyang.ga:7373/index.html?=" + str(randomNumber))
		#选择回帖
		pyautogui.click(476,522,duration=0.25)
		#选择经营
		pyautogui.click(462,586,duration=0.25)
		#提交报送
		pyautogui.click(900,666,duration=0.25)
		time.sleep(1)
		

#定义一个宣传类提交函数
def submitXuanchuan():	
	for i in range(11):
		#点击我要报送
		pyautogui.click(53,354,duration=0.25)
		#点击地址栏
		pyautogui.click(413,345,duration=0.25)
		#输入网址加随机值
		randomNumber = random.randint(100000000,999999999)
		pyautogui.typewrite("http://dongyang.ga:7373/index.html?=" + str(randomNumber))
		#选择主帖
		pyautogui.click(409,522,duration=0.25)
		#选择宣传
		pyautogui.click(511,586,duration=0.25)
		#提交报送
		pyautogui.click(900,666,duration=0.25)
		time.sleep(1)
	



for i in range(5):

	#以下这段代码为切换id
	#选择身份栏
	pyautogui.click(766,458,duration=0.25)
	#选择身份
	pyautogui.press(['down'])
	pyautogui.press('enter')
	#点击确定
	pyautogui.click()
	time.sleep(1)
	#开始填写经营类表单并提交
	submitJingying()
	#重新回到首页，准备选择的下个id
	pyautogui.click(53,354,duration=0.25)
	#提交后停顿片刻
	time.sleep(1)


#最后提交十个宣传类url，id是哪个无所谓
submitXuanchuan()

pyautogui.alert('完成')
