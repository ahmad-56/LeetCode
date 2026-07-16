num = 38

condition = False
ans = 0
while condition == False:
    for i in range(len(str(num))):
        ans += int(str(num)[i])
    if len(str(ans)) == 1:
        condition = True
    else:
        num = ans
        ans = 0

print(ans)