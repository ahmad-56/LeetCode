class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        for i in nums:
            if i not in seen:
                if nums.count(i) == 1:
                    return i
                    break
                elif i not in seen:
                    seen.append(i)