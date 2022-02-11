from unittest import TestCase
from ddt import data, ddt, unpack
from bread_first_search import BreadFirstSearch as BFS

@ddt
class TestBreadFirstSearch(TestCase):
    @data(
        [(0,1), (2,3), 4],
        [(0,1), (0,1), 0],
        [(2,3), (0,1), 4],
        [(0,0), (0,3), 0],
        [(3,2), (0,1), 0],
        [(0,1), (2,1), 2],
    )
    @unpack
    def test_(self, start, end, expect_path):
        data = [
            [0,1,0,0],
            [1,1,1,1],
            [1,1,0,1],
            [0,0,1,0]
        ]
        res=BFS().iterativeShortestPath(data,start,end)
        #print(res)
        assert res[0] == expect_path

    
    @data(
        # [ [[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2,
        #     [[2,2,2],[2,2,0],[2,0,1]] ], 
        # [ [[0,0,0],[0,0,0]], 0, 0, 2,
        #     [[2,2,2],[2,2,2]] ],
        [ [[0,0,1],[0,1,1]], 1, 1, 1, [[0,0,1],[0,1,1]]]
    )
    @unpack
    def test_floodFill(self, image, sr,sc,color, expect_res):
        res = BFS().floodFill(image,sr,sc,color)
        # print(res)

    
    @data(
        [ [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],\
            [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],\
            [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],\
            [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6],
        [[[0,0,0,0,0,0,0,0]], 0],
    )
    @unpack
    def test_(self, data, expect_res):
        res= BFS().maxAreaOfIsland(data)
        print(res)