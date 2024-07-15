# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
    
        for num in nums[1:]: # it will start from index 1 and not 0
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
    
        return max_global
    
"""
1. The loop starts from the second element (for num in nums[1:]).
2. max_current is updated to be the maximum of the current element itself (num) or the current element plus max_current (max_current + num).
3. max_global is updated to be the maximum of max_global or max_current whenever max_current is updated.
4. max_global holds the maximum sum of any contiguous subarray by the end of the iteration.
"""