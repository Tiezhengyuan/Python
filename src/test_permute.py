from unittest import TestCase
from ddt import data, ddt, unpack
from permute import Permute as S

@ddt
class TestPermute(TestCase):
    '''
    @data(
        ["abc", ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']],
        ["a",["a"]],
        ["",[]]
    )
    @unpack
    def test_permute(self,data, expect_res):
        res = S().permuteString(data)
        # print(res)
        assert res ==expect_res


    @data(
        ["ab", "eidbaooo", True],
        ["ab", "eidboaoo", False],
        ["ab", "b", False],
        ["dinitrophenylhydrazine", "acetylphenylhydrazine", False],
        ["adc", "dcda", True],
        ["hello", "ooolleoooleh", False],
        ["trinitrophenylmethylnitramine", \
            "dinitrophenylhydrazinetrinitrophenylmethylnitramine", True]
    )
    @unpack
    def test_checkInclusion(self,s1,s2, expect_res):
        res = S().checkInclusion(s1,s2)
        #print(res)
        assert res == expect_res
    '''

    @data(
        [['a','b','c', 'd'], 2, []],
    )
    @unpack
    def test_combineList(self, data, m, expect_res):
        res = S().combineList(data, m)
        print(res)
        #assert res ==expect_res