gain = [-4,-3,-2,-1,4,3,2]
res = []
res.append(0)
for i in gain:
    net = res[-1] + i
    res.append(net)
print(max(res))
