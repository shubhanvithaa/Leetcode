a = "10"
b = "1"

# Make lengths equal
len_a = len(a)
len_b = len(b)
a = a.zfill(max(len_a, len_b))
b = b.zfill(max(len_a, len_b))

# Reverse for processing from LSB to MSB
a = a[::-1]
b = b[::-1]

res = ""
carry = 0
len_str = len(a)

for i in range(len_str):
    bit_a = int(a[i])
    bit_b = int(b[i])

    sum_bits = bit_a + bit_b + carry
    res += str(sum_bits % 2)  # Append sum modulo 2
    carry = sum_bits // 2  # Update carry

# If there's a carry left, add it
if carry:
    res += "1"

# Reverse back to get final binary result
res = res[::-1]

print(res)  # Expected output: "11"
