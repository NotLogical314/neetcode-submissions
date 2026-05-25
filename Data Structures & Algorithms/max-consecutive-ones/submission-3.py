class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        result = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                result = max(ones, result)
                ones = 0
        return  max(result, ones)