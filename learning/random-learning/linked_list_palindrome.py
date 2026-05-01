

# num = 0
# rev = 0
# tens = 1
# while (head.next):
#     num = num*10+head.val
#     rev = head.val*tens+rev
#     tens*=10

#     head = head.next
# return (num==rev)


list1 = [1,2]

num = 0
rev = 0
tens = 1
for i in list1:
    num = num*10+i
    rev = i*tens+rev
    tens*=10

    
print(num==rev)