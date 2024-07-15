class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target: # 0 degree rotation
                return True
            mat = [list(row) for row in zip(*mat[::-1])] # 3 rotations : 90, 180, 270
        return False

"""
Explanation:

1. [list(row) for row in zip(*mat[::-1])] rotates a given matrix by 90 degrees clockwise. It first reverses the rows of the matrix and then transposes it using zip.

2. findRotation function:
This function checks if the matrix mat matches the target matrix. It tries four rotations (0 degrees, 90 degrees, 180 degrees, 270 degrees) by repeatedly rotating the matrix and comparing it to the target.

3. [list(row) for row in zip(*mat[::-1])] very important
"""