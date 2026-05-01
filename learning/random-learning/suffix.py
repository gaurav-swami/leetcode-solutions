arr = [1, 2, 3, 4, 5]
suffix = [0] * len(arr)

# Correct initialization: Last element of suffix is the last element of arr
suffix[-1] = arr[-1]

# Fill suffix from right to left
for i in range(len(arr) - 2, -1, -1):
    suffix[i] = suffix[i + 1] * arr[i]

print(suffix)