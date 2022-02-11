
from typing import List
import re
class Permute:
    def __init__(self):
        self.pool = []

    def permuteList(self, s:List[chr], L:int, R:int):
        if L == R:
            self.pool.append("".join(s))
        else:
            for i in range(L, R+1):
                s[L], s[i] = s[i], s[L]
                self.permuteList(s, L+1, R)
                s[L], s[i] = s[i], s[L]

    def permuteString(self, s: str):
        L, R = 0, len(s)
        self.permuteList(list(s), L, R-1)
        return self.pool

    def combineElement(self, s, L, R, m, pool):
        if L == m:
            # print(s[:L])
            pool.append(s[:L])
        else:
            for i in range(L, R+1):
                s[L], s[i] = s[i], s[L]
                self.combineElement(s, L+1, R, m, pool)
                s[L], s[i] = s[i], s[L]

    def combineList(self, s: List, m: int):
        L, R = 0, len(s)-1
        pool = []
        self.combineElement(s, L, R, m, pool)
        return pool


    def sortStr(self, s):
        s = list(s)
        s.sort()
        s = "".join(s)
        # print(s)
        return s

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = self.sortStr(s1)
        s1_len = len(s1)
        # print("s1=", s1)

        for i in range(0, len(s2)-len(s1)+1):
            sub = self.sortStr(s2[i:i+s1_len])
            # print(sub)
            if sub==s1:
                return True
        return False




