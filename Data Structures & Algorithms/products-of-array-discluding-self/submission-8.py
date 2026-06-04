class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums)-1, -1 , -1):
            ans[j] *= suffix
            suffix *= nums[j]

        return ans