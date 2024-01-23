def ispalindrome(s):
    a=0
    b=len(s)-1
    while a<b:
        if s[a].lower()!=s[b].lower():
            return False
        a+=1
        b-=1
    return False

ispalindrome("radar")    