class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum = []
        sum = 0

        for num in nums:
            sum += num
            presum.append(sum)

        for n in range(len(nums)):
            left = presum[n - 1] if n > 0 else 0
            right = presum[-1] - presum[n]
            if left == right:
                return n

        return -1