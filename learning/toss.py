import random

count_ronit = 0
count_gaurav = 0
count_shubham=0
for i in range(100):
	randoms = random.randint(1,3)
	if (randoms==1):
		count_ronit+=1
	elif (randoms==2):
		count_gaurav+=1
	elif (randoms==3):
		count_shubham+=1


print("Ronit Ke =", count_ronit)
print("Gaurav Ke =", count_gaurav)
print("Shubham Ke =", count_shubham)