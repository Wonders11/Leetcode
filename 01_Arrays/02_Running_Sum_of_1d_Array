class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # it will skip 0th index element and start calculating from index 1 to index N-1 
        for i in range(1,N):
            nums[i] += nums[i-1]

        return nums