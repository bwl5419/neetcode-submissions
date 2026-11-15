class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        allt = []
        for row in matrix:
            for item in row:
                allt.append(item)
        if target in allt:
            return True
        return False