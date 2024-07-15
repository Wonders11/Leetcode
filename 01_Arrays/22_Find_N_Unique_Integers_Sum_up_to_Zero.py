class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
    
        # If N is odd, include 0
        if n % 2 != 0:
            result.append(0)
            n -= 1  # We now need N-1 more numbers

        # Add pairs of numbers
        for i in range(1, n // 2 + 1): # pairs will start from 1,-1 and so on
            # N // 2 (inclusive)
            result.append(i)
            result.append(-i)
    
        return result
    
"""
Approach
If N is odd: We can include 0 in the list and then pairs of positive and negative integers.
If N is even: We only need pairs of positive and negative integers.

Generating Pairs:
For the remaining N (which is now even), we generate pairs (i, -i) using a loop from 1 to N // 2 (inclusive).
Each iteration adds a positive number i and its corresponding negative -i to the result list.

"""