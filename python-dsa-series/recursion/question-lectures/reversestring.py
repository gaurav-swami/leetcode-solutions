def palindrome(s,l=0,r=None):
    if not r:
        r = len(s)-1
    if l>=r:
        return True
    if s[l] != s[r]:
        return False 
    return palindrome(s, l+1, r-1)


s = "kanak"
print(palindrome(s))
