from typing import List

from ddt import ddt
class BreadFirstSearch:

    def getNextPoints(self, image, point):
        row = len(image)
        col = len(image[0])
        next_points = []
        i,j = point
        if i-1>=0 and image[i-1][j] != 0:
            next_points.append((i-1, j))
        if j-1>=0 and image[i][j-1] != 0:
            next_points.append((i,j-1))
        if i+1<row and image[i+1][j] != 0:
            next_points.append((i+1,j))
        if j+1<col and image[i][j+1] != 0:
            next_points.append((i,j+1))
        return next_points

    def iterativeShortestPath(self, image: List[List[int]], start, end):
        x=image[start[0]][start[1]]
        y=image[end[0]][end[1]]
        #print(f"detect path {start}:{x}->{end}:{y}")
        paths=[]
        shortest = 0
        #check invalid start and end point
        if image[start[0]][start[1]]==0 or image[end[0]][end[1]]==0:
            return 0, []
        #suppose pool is queue type
        pool=[[start]]
        while pool:
            node= pool.pop(0)
            if node[-1] == end:
                if shortest == 0 or len(node)==shortest:
                    paths.append(node)
                    shortest = len(node)-1
                elif len(node) < shortest:
                    paths = [node]
                    shortest = len(node)-1
            else:
                next_points = self.getNextPoints(image, node[-1])
                for p in next_points:
                    #check circle access
                    if p not in node: 
                        pool.append(node+[p])
        return shortest, paths

    def getNextPoints2(self, image, point):
        row = len(image)
        col = len(image[0])
        next_points = []
        i,j = point
        if i-1>=0: next_points.append((i-1, j))
        if j-1>=0: next_points.append((i,j-1))
        if i+1<row: next_points.append((i+1,j))
        if j+1<col: next_points.append((i,j+1))
        return next_points

    def floodFill(self, image: List[List[int]], sr: int, \
        sc: int, newColor: int) -> List[List[int]]:

        row = len(image)
        col = len(image[0])
        if sr<0 or sr>=row or sc<0 or sc>=col:
            return []
            
        pool = [(sr,sc)]
        target_val = image[sr][sc]
        access = {sr:[sc]}
        while pool:
            point = pool.pop(0)
            # print(point)
            next_points = self.getNextPoints2(image, point)
            for p in next_points:
                x,y=p
                if x in access and y in access[x]:
                    continue
                if image[x][y]==target_val:
                    image[x][y]=newColor
                    pool.append(p)
                    if x in access: access[x].append(y)
                    else: access[x]=[y]
        image[sr][sc]=newColor
        return image     

    def calArea(self, grid, i, j):
        pool=[(i,j)]
        nodes = [(i,j)]
        while pool:
            point = pool.pop(0)
            next_points = self.getNextPoints(grid, point)
            #print(f"{point}->{next_points}")
            for p in next_points:
                if p not in nodes:
                    grid[p[0]][p[1]]=0
                    nodes.append(p)
                    pool.append(p)
            grid[i][j]=0
        return grid, len(nodes)
            


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col= len(grid[0])
        i,j = 0,0
        max_area=0
        while i<row and j<col:
            #print(i,j)
            if grid[i][j]==1:
                grid, area = self.calArea(grid, i, j)
                if area> max_area: max_area = area
                # print(f"Start{(i,j)}. area={area}")
            else:
                if j<col-1:
                    j+=1
                elif j==col-1:
                    i+=1
                    j=0
        return max_area

