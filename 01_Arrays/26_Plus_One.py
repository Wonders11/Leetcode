class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        # Traverse the digits from the last to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we finish the loop, it means we had a carry from the most significant digit
        return [1] + digits
    
"""
Explaination

Initialization:
Determine the length of the digits array.

Traverse from the Last Digit:
Use a for-loop to iterate from the end of the array to the beginning.

Increment and Check for Carry:
If the current digit is less than 9, increment the digit and return the array (no carry beyond this point).
If the current digit is 9, set it to 0 (carry to the next digit).

Handle Remaining Carry:
If the loop completes, it means all digits were 9, and the result is an array with a leading 1 followed by zeros.
"""