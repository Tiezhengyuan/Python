from copy import deepcopy
from unittest import TestCase, skip
from ddt import ddt, data, unpack
from src.matrix_BSF import MatrixBSF

@ddt
class testMatrixBSF:
    def setUp(self):
        self.solution = MatrixBSF()
    
    @data(
        [[[0,0,0],[0,1,0],[0,0,0]],
            [[0,0,0],[0,1,0],[0,0,0]]],
    )
    @unpack
    def test_updateMatrix(self, data, expect):
        res = self.solution.updateMatrix(data)
        print(res)