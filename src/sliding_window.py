from typing import List, Dict

class SlidingWindow:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        detect the length of the longest substring
        """
        if len(s) == 0:
            return 0

        #string should consist of at least one character
        L, R = 0, 1
        max_len = sub_len = R - L
        while L < R and R < len(s):
            # print(f"{L}->{R}\t{s[L:R]}", end="\t")
            sub = s[L:R]
            res = sub.find(s[R])
            if res >= 0:
                L = L+ res + 1
            R += 1
            sub_len = R - L
            if sub_len > max_len:
                max_len = sub_len
            # print(f"{res}:{L}->{R}\t{s[L:R]}")
        return max_len

    def max_sum_subarray(self, arr, size) -> List:
        """
        Given an array of integers, find 
        maximum sum subarray of the required size.
        """
        if 0 <= len(arr) <= size:
            return arr
        
        max_sum, max_arr = 0, []
        for L in range(len(arr)-size+1):
            R = L + size
            window_sum = sum(arr[L:R])
            if window_sum > max_sum:
                max_sum = window_sum
                max_arr = arr[L:R]
            # print(f"{L}-{R}-{arr[L:R]}")
        return max_arr

            
