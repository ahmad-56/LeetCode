#strs = ["a"]
strs = ["flower","flow","flight"]
L_C_P_word = ""
smallest = 0
#smallest word in list:
for word in range(len(strs)):
    if len(strs[word]) <= len(strs[word-1]):
        smallest = len(strs[word])

#compare
array = []
condition = False
while condition == False:
    for i in range(len(strs)):
        word = strs[i]
        array.append(word[:smallest])
    for j in range(len(array)-1):
        if array[j] != array[j+1]:
            array = []
            smallest -= 1
            break
        if array.count(array[0]) == len(array):
            condition = True
            break

L_C_P_word = array[0]
print(f"LCP: {L_C_P_word}")