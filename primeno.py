#!/python/3
import math

num = 13

for m in range (2,math.sqrt(num)):
	if m / num == 0:
		print(num, "is prime")
		break
	else:
		print(num, "is not prime")
