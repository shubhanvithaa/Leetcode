a = "1"
b = "111"



len_a = len(a)
len_b = len(b)
a = a.zfill(len_b)
b = b.zfill(len_a)
a = a[: : -1]
b = b[: : -1]
len_a = len(a)
len_b = len(b)
carry =0
res = ''
for i in range(len_a):
    bit_a = int(a[i])
    bit_b = int(b[i])

    res += str((bit_a + bit_b + carry)%2)
    carry = (bit_a + bit_b + carry)//2

if (carry == 1):
    res+="1"
res =  res[::-1]
print(res)  # Expected output: "11"

