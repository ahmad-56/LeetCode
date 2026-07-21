class Solution:
    def isHappy(self, n):

        n = list(str(n))
        ans = 0
        condition = False
        stored = []

        while True:
            for i in n:
                ans += int(i) ** 2
            if ans == 1:
                condition = True
                break
            elif ans in stored:
                break   
            else:
                stored.append(ans)
                n = list(str(ans))
                ans = 0

        return condition
    
num = Solution()
result = num.isHappy(19)
print(result)