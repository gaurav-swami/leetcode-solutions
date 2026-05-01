lst = []

def permutations(s, current=""):
    if len(s) == 0:
        lst.append(current)
       
        return
    
    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        permutations(remaining, current + ch)

word = "aspire"
permutations(word)

new_lst = sorted(lst)


new_lst.index("aspire")

print(new_lst.index("aspire")+1)