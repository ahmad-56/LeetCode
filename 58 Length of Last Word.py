#s = "   fly me   to   the moon  " # return 4
#s = "Hello World" # return 5
s = " a" # rertun 1

pos = 0
length = 0
reached = False
start = 0
end = 0
finish = False

if len(s) == 1:
    print(1)
else:
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " " and reached == False:
            end = i + 1
            reached = True
        elif s[i] == " " and reached == True:    
            start = i + 1
            finish = True
        if finish == True:
            break  

    word = s[start:end]
    length = len(word)
    print(length)
    print(word)