class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1

        sorted_dict = sorted(dict.items(), key= lambda x: x[1] , reverse=True)

        return([key for key , value in sorted_dict[:k]])