class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initializing empty hashmap (dictionary in python)
        num_to_index = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
    
        # According to the problem statement, there will always be exactly one solution,
        # so this line should never be reached.
        return []

"""
Explaination with input: Input: nums = [3,2,4], target = 6

First Iteration (i = 0, num = 3):

Calculate the complement: complement = 6 - 3 = 3.
Check if the complement (3) is in the dictionary num_to_index. It is not.
Add the number 3 and its index 0 to the dictionary: num_to_index = {3: 0}.

Second Iteration (i = 1, num = 2):

Calculate the complement: complement = 6 - 2 = 4.
Check if the complement (4) is in the dictionary num_to_index. It is not.
Add the number 2 and its index 1 to the dictionary: num_to_index = {3: 0, 2: 1}.

Third Iteration (i = 2, num = 4):

Calculate the complement: complement = 6 - 4 = 2.
Check if the complement (2) is in the dictionary num_to_index. It is.
The complement 2 is found in the dictionary with index 1. Therefore, we have found the solution: the numbers at indices 1 and 2 (values 2 and 4) add up to 6.
"""