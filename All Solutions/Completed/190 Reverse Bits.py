n = 43261596
#n = 2147483644

array = []
for c in range(32):
    array.append(0)

#converting to binary
for i in range(31, 0, -1):
    if 2 ** i <= n:
        n -= 2 ** i
        array[-i-1] = 1

b1 = ""
for j in array:
    b1 += str(j)

b2 = b1[::-1]
ans = 0
for i in range(32):
    if b2[i] == "1":
        ans += 2 ** (31-int(i))

print(ans) #964176192
print(b1)
print("00000010100101000001111010011100")