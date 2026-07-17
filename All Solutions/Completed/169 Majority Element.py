nums = [2,2,1,1,1,2,2,3,3,3,3,3,3,3,3,3]

seen = []
for i in nums:
    if i not in seen:
        if nums.count(i) >= len(nums)/2:
            print(i)
            break
        elif i not in seen:
            seen.append(i)