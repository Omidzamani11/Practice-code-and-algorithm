def strStr23(s,x):
  if x not in s:
    return -1
  n = len(x)
  for i in range(len(s)):
    print(i)
    
    if s[i:i+n] == x :
      return i
  return -1
strStr23 ("omid","id")