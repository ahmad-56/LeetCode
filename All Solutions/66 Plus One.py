digits = [1,2,3,9]

num = ""
if digits[-1] == 9:
    for i in digits:
        num += str(i)
    num = int(num)
    num += 1
    digits = []
    for j in str(num):
        digits.append(int(j))
else:
    digits[-1] += 1

print(digits)