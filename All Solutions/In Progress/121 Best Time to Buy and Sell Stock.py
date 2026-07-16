prices = [7,1,5,3,6,4]

max_num = 0
min_num = prices[0]
for i in range(len(prices)):
    if prices[i] < min_num:
        min_num = prices[i]
    elif prices[i] > max_num:
        max_num = prices[i]

best = max_num - min_num
print(best)