candies = [2, 3, 5, 1, 3]
extraCandies = 3
copy =[]
for i in candies:
    copy.append(i)
candies.sort(reverse = True)
high = candies[0]
res = []
for i in copy:
    if i+extraCandies > high or i+extraCandies == high:
        res.append(True)
    else:
        res.append(False)
print(res)