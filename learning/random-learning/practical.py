def encode(str): return "".join([chr(ord(i)+1) for i in str])
def pincode(num): return sum(int(i) for i in str(num))
def fact(num): return 1 if int(num)<=1 else int(num)*fact(int(num)-1)

dictk = {	
	"What is your age?": fact, 
	"What is your pincode?": pincode, 
	"What is your name?": encode
}

while dictk: 
	for key,value in dictk.items(): 
		print(value(input(key + " : ")))
