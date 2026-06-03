class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0

        for num in nums:
            currsum = max(currsum , 0) + num
            maxsum = max(currsum , maxsum)

        return  maxsum