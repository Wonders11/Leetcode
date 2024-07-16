class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
"""
1. Calculate the midpoint mid of the current search range.

2. Calculate the total number of coins required to form mid rows using the formula for the sum of the first mid natural numbers: mid * (mid + 1) / 2.

3.Compare this total with n:
If the total equals n, return mid.
If the total is less than n, move the search range to the right (left = mid + 1).
If the total is greater than n, move the search range to the left (right = mid - 1).

Convergence: The search range converges to the maximum number of complete rows.
"""