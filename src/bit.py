from typing import List

class Bit:

    def isPowerOfTwo(self, x):
        """
        check if x is the power of 2
        """
        if x == 0: return False
        adj_bit = x & (x - 1)
        return not adj_bit
    
    def countOnes(self, x):
        """
        count number of ones of x
        """
        counts = 0
        while x > 0:
            counts += 1
            x = x & (x-1)
        return counts

    def largestPowerOfTwo(self, x):
        """
        Given x, return the largest number
        which is the power of 2
        """
        if x < 2: return None
        p = x & (x - 1)
        if p == 0: return x
        return self.largestPowerOfTwo(p)

    def reverseBits(self, x):
        """
        reverse bits of integer
        """
        y = 0
        while x > 0:
            y = (y << 1) + (x & 1)
            x = (x >> 1)
        return y

    def singleNumber(self, nums:List):
        """
        detect single number in a list of which
        most elements have one duplicate
        """
        tmp = []
        while nums:
            el = nums.pop()
            if el in tmp or el in nums:
                tmp.append(el)
            else:
                return el
        return None
