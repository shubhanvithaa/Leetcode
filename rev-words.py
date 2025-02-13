s = "  hello world  "
res = ''
s = s.split(' ')
s = s[: : -1]
res = ' '.join(s)
if (res[1] or res[-1] ==' '):
    res.replace(' ','')
    
print(res)

#solution 2
print(' '.join(s.split()[::-1]))