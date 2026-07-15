n = 1
sumEven = 0
sumOdd = 0
count = 0
i = 1

if n == 1:
    print(1)
else:
    while count != n:
        sumOdd += i
        sumEven += i+1
        i += 2
        count += 1

    gcd = 0
    for i in range(1, sumOdd):
        if sumOdd % i == 0 and sumEven % i == 0:
            if i >= gcd:
                gcd = i

    print(gcd)