s = "A man, a plan, a canal: Panama"
new = ""
for i in s:
    if i.isalnum() == True:
        new += i.lower()
check = new[::-1]
if new == check:
    print(True)    
else:
    print(False)