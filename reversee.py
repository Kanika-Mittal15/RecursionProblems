def revrse(s):
    if len(s)==0 or len(s)==1:
        return  s
    else:
        return s[len(s)-1]+revrse(s[:len(s)-1])

s=str(input())
print(revrse(s))