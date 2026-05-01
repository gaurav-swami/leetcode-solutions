def functions(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return functions(n-1) + functions(n-2)

for i in range(10):
	print(functions(i) ,end=" ")