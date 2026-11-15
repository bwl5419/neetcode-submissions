class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        clean= []
        for row in matrix:
            for item in row:
                clean.append(item)
        if target in clean:
            return True
        return False