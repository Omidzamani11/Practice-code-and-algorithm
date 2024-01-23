def ispalindrome(s):
    a = 0
    b = len(s) - 1
    while a < b:  # اصلاح شرط
        if s[a].lower() != s[b].lower():
            return False
        a += 1  # اصلاح افزایش شمارنده
        b -= 1  # اصلاح کاهش شمارنده
    return True  # اگر تمام کاراکترها برابر باشند


print(ispalindrome("radar"))
