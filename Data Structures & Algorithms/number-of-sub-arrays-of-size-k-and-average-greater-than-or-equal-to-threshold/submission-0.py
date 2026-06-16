class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        count = 1 if (window_sum/k) >= threshold else 0

        for right in range(k , len(arr)):
            window_sum += arr[right] - arr[right - k]
            if (window_sum/k) >= threshold:
                count += 1
        
        return count