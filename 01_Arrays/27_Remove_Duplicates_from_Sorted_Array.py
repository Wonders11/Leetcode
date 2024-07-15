class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # If the input array is empty, return 0.
        if not nums:
            return 0
    
        # Initialize the second pointer
        j = 0
    
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
    
        return j + 1