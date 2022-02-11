from typing import List

class MatrixBSF:

    #def orangesRotting(self, grid: List[List[int]]) -> int:
    
    def adj_coord(self, row: int, col: int, \
        current_coord:tuple)->List:
        x, y = current_coord
        pool = []
        if x-1 >=0:
            pool.append((x-1, y))
        if y-1 >=0:
            pool.append((x, y-1))
        if y+1 < col:
            pool.append((x, y+1))
        if x+1 < row:
            pool.append((x+1, y))
        return pool

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Given an m x n binary matrix mat, 
        return the distance of the nearest 0 for each cell.
        The distance between two adjacent cells is 1.
        """
        row = len(mat)
        col = len(mat[0])
        new_mat = [[0]*col]*row
        pool = [(0,0)]
        while pool:
            current = pool.pop(0)
            adj_points = self.adj_coord(row,col, current)