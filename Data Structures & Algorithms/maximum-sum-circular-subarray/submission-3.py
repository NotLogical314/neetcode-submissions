class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        minsum = 0
        total = 0
        currmin = 0

        for num in nums:
            total += num

            currsum = max(currsum , 0) + num
            maxsum = max(currsum , maxsum)

            currmin = min(currmin , 0) + num
            minsum = min(currmin , minsum)

        if maxsum < 0:
            return maxsum
            
        return max(maxsum , total - minsum)
        