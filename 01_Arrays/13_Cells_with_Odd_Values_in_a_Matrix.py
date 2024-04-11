# Good Question
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initializing matrix of size m*n with 0
        matrix = [[0]*n for _ in range(m)] # move from right to left -> rows to columns

        # iterating through indices and incrementing matrix elements
        for r,c in indices:
            for i in range(m):
                matrix[i][c] += 1
            for j in range(n):
                matrix[r][j] += 1

        odd_count = sum(1 for row in matrix for cell in row if cell % 2 != 0)

        return odd_count