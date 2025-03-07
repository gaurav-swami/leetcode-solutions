#question 1
'''

arr = [1,2,2,3,3,3]
freq = {}

for i in arr:
	if i in freq:
		freq[i]+=1
	else:
		freq[i] = 1

print(freq)


arr = [1,2,3,3,4]
dup = {}
for i in arr:
	if i in dup:
		print(True)
	else:
		dup[i] = 1
'''

s = "aabbcdde"

rep = {}
for i in s:
	if i in rep:
		rep[i]+=1
	else:
		rep[i] = 1

for i in rep:
	if rep[i]==1:
		print(i)

print(rep)
