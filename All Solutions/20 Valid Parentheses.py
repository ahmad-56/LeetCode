s = """](){}"""

dict = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
}

situation = True

for i in range(len(s)):
    if s.index(")") < s.index("(") or s.index("]") < s.index("[") or s.index("}") < s.index("{"):
        situation = False
#    check = s[i:s.index(dict[s[i]])+1]
#    print(check)

print(situation)