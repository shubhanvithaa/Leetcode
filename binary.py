a = ""
b = ""
len_a = len(a)
len_b = len(b)
a = a.zfill(len_b)
b = b.zfill(len_a)
res = []
carry = 0
len_str = len(a)
a = a[: : -1]
b = a[: : -1]
for i in range(len_str):
    if(a[i] != b[i]):
        res.append()
        carry = 0
        
print(res)