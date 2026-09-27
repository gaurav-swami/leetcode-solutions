a = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0
#1 2 3
#4 5 6
#7 8 9
def printmat(a):
    for i in range(len(a)):
        for j in range(len(a[0])):

            print(a[i][j],end = " ")
        print()
print()
for i in range(len(a)):
    for j in range(0,i+1):
        print(a[i][j],end = " ")
    print()
print()                       
for i in range(len(a)):
    print("  "*i, end = "")
    print(a[i][i])

print()
for i in range(len(a)):
    print("  "*(2-i), a[i][2-i])


print("transpose of a matrix")

mat = [[5,9,1], [2,3,7]]
rows = len(mat)
cols = len(mat[0])
new_mat = [ [0]*rows for _ in range(cols) ]

for i in range(rows):
    for j in range(cols):
        new_mat[j][i] = mat[i][j]

print(new_mat)
printmat(new_mat)
