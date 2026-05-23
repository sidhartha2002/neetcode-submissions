class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        
        for i in range(numRows):
            # Create a row of '1's with the correct length (row 0 has 1 element, row 1 has 2, etc.)
            row = [1] * (i + 1)
            
            # Update the interior elements (skip the first and last element)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            # Add the finished row to our triangle
            triangle.append(row)
            
        return triangle