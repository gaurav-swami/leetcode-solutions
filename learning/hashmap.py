from collections import defaultdict

d = {'greg':1,'steve':2,'steve':3}
print(d)

d['arsh']=4

if d['arsh']:
	print(d['arsh'])


for key,val in d.items():
	print(key,":",val)


defaultdict = defaultdict(int)