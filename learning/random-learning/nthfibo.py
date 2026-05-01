def nthfibo(n):
	i=0
	j=1
	count = 1
	while count < n:
		i,j = j,j+i
		count+=1

	return i


print(nthfibo(7))
