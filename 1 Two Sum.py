class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        for i in range(0, len(self.nums)):
            for j in range(i+1, len(self.nums)):
                num_1 = i
                num_2 = j
                if int(self.nums[num_1]) + int(self.nums[num_2]) == self.target:
                    print(f'[{num_1},{num_2}]')
                    return([num_1,num_2])