
def isAnagram( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s)!=len(t):
        return False
    else:
        for i in s:
            if i not in t:
                return False
        return True


s1,t1 = "anagram", "nagaram"
s2,t2 = "rat", "car"

print(isAnagram(s2,t2))