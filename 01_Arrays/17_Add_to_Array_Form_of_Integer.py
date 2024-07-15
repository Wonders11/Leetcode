class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Convert K to a list of digits
        k = list(map(int, str(k)))
    
        # Initialize pointers for A and K
        i, j = len(num) - 1, len(k) - 1
    
        carry = 0
        result = []
    
        # Process each digit from the end of both arrays
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry = carry +  num[i]
                i = i - 1
            if j >= 0:
                carry = carry +  k[j]
                j = j - 1
        
            result.append(carry % 10)
            carry //= 10
    
        # Reverse the result since we've been adding digits from the least significant digit
        return result[::-1]
    
    """
Explanation:
1. Convert K to a list of its digits.
2. Use two pointers i and j to track the current digits in A and K respectively, starting from the end.
3. Initialize a carry variable to handle sums greater than 9.
4. Loop through the digits of A and K, adding them along with any carry.
5. Append the result of (current sum % 10) to the result list.
6. Update the carry as (current sum // 10).
7. If there are remaining digits in A or K or there's a carry, continue the loop.
8. Finally, reverse the result list since we collected digits from least significant to most significant.
    """