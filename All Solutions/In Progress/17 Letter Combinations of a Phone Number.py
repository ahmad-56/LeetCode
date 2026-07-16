digits = "234"

two = ["a","b","c"]
three = ["d","e","f"]
four = ["g","h","i"]
five = ["j","k","l"]
six = ["m","n","o"]
seven = ["p","q","r","s"]
eight = ["t","u","v"]
nine = ["w","x","y","z"]

num = {
    "2" : two,
    "3" : three,
    "4" : four,
    "5" : five,
    "6" : six,
    "7" : seven,
    "8" : eight,
    "9" : nine
}

new = []
for i in range(1, len(digits)):
    new.append(num[digits[i]]) 

array = []
if len(digits) == 1:
    array = num[digits]
else:
    for j in range(len(new)):
        for k in range(len(new[j])):  
            for d in range(len(num[digits[0]])):
                combinations = num[digits[0]][d] + new[j][k]
                array.append(combinations)

print(array) #["ad","ae","af","bd","be","bf","cd","ce","cf"]