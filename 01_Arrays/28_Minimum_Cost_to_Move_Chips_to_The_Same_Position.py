class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        even_count = 0
        odd_count = 0
    
        # Count the number of chips at even and odd positions
        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
        # The minimum cost will be the smaller count of even and odd positions
        return min(even_count, odd_count)