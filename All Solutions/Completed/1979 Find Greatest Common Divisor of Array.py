nums = [2,5,6,9,10]

max_num = max(nums)
min_num = min(nums)

for i in range(1, max_num + 1):
    if max_num % i == 0 and min_num % i == 0:
        num = i

print(num)