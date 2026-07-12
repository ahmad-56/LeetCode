class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        check = text[::-1]
        if check == text:
            return True
        else:
            return False