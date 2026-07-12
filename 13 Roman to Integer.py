dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    "A" : 0
}
        
total = 0 
s= "MCDLXXVII" #1476

#if s[-1] == "V" or s[-1] == "L" or s[-1] == "D":
#    num = len(str(s)) - 2
#    for i in range(num):
#        total += dict[s[i]]
#    total += dict[s[-1]]
#    total -= dict[s[-2]]
#    print(total)

if  len(s) % 2 != 0: 
    s += "A"

for i in range(0, len(s), 1):
    check = s[i:i+2]
    if check[0] == "I" and (check[-1] == "V" or check[-1] == "X"):
        total -= 1
    elif check[0] == "X" and (check[-1] == "L" or check[-1] == "C"):
        total -= 10
    elif check[0] == "C" and (check[-1] == "D" or check[-1] == "M"):
        total -= 100
    else:
        total += dict[s[i]]

print(total)