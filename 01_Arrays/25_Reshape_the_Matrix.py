class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Get the number of rows and columns of the original matrix
        m, n = len(mat), len(mat[0])
    
        # Check if the reshaping is possible and if not then return original matrix
        if m * n != r * c:
            return mat
    
        # Flatten the original matrix
        flat_list = [num for row in mat for num in row]
        # here first row in mat is called and then num is row once this is completed it will come to outer loop
    
        # Create the new reshaped matrix
        new_matrix = []
        for i in range(r):
            new_matrix.append(flat_list[i * c:(i + 1) * c])
    
        return new_matrix
