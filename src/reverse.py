from typing import List
class Reverse:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L, R = 0, len(s)-1
        while L < R:
            s[L], s[R] = s[R], s[L]
            L+=1
            R-=1

    def gen_words(self, sentence: str):
        """
        """
        for w in sentence.split(" "):
            yield w

    def reverseWords(self, s: str) -> str:
        """
        """
        s2 = []
        gen = self.gen_words(s)
        for word in gen:
            s2.append(word[::-1])
        reversed = " ".join(s2)
        return reversed
