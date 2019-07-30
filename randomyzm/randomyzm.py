import random
temp = ''
for i in range(6):
	num = random.randrange(0,2)
	if num == 1:
		rad2 = random.randrange(0,10)
		temp = temp + str(rad2)
	else:
		rad1 = random.randrange(65,91)
		c1 = chr(rad1)
		temp = temp + c1
print(temp)