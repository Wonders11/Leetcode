class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Find the minimum value in each row
        min_in_rows = {min(row) for row in matrix}
    
        # Transpose the matrix to easily find the maximum value in each column
        transposed_matrix = list(zip(*matrix))
        max_in_columns = {max(column) for column in transposed_matrix}
    
        # The lucky numbers are the intersection of min_in_rows and max_in_columns
        lucky_numbers = list(min_in_rows & max_in_columns)
    
        return lucky_numbers
    
"""
zip(*matrix) - Tranpose of matrix - rows to columns and columns to rows
"""