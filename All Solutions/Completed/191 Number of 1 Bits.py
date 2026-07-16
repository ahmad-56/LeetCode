n = 11

array = []
for c in range(32):
    array.append(0)

#converting to binary
for i in range(31, 0, -1):
    if 2 ** i <= n:
        n -= 2 ** i
        array[-i-1] = 1

if n % 2 != 0:
    array[-1] = 1

print(array.count(1))
print(array)