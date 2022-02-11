from typing import List

class RecursionString:
    def __init__(self):
        self.target = []

    def reverse_str(self, data):
        if not isinstance(data, str):
            return None
        if len(data)<=1:
            return data
        return data[-1]+self.reverse_str(data[:-1])
    
    def count_instance(self, s:str, target:str) -> int:
        if not isinstance(s, str):
            return None
        if len(s)<=0:
            return 0
        if s[0]== target:
            return 1 + self.count_instance(s[1:], target)
        return 0 + self.count_instance(s[1:], target)


    def is_palindrome1(self, s):
        #check if a string is palindrome
        #returns if the string is a palindrome. 
        # string is equal to its reverse
        if len(s)> 1 :
            return bool(s[::-1] == s)
        return False
    
    def is_palindrome(self, s):
        if len(s) == 1:
            return True
        elif len(s) >= 2:
            if s[0] == s[-1]:
                if len(s) == 2:
                    return True
                return self.is_palindrome(s[1:-1])
        return False
        
    def detect_palindrome(self, s:str, seed: int):
        """
        #extend palindrome sub-string as long as it can
        #input_str[start:end] must be palindrome
        """
        if seed > 2 and len(s) >= seed:
            #determine the best seed
            for L in range(len(s)-2):
                if s[L] == s[L+1]:
                    self.expand_palindrome(s, L, L+1)
                if s[L] == s[L+2]:
                    self.expand_palindrome(s, L, L+2)
        return self.target


    def expand_palindrome(self, s, L, R):
        if L > 0 and R < len(s)-1:
            ns = s[(L-1):(R+2)]
            if ns[0] == ns[-1]:
                return self.expand_palindrome(s, L-1, R+1)
        if len(self.target) > 0:
            current = self.target[0]
            if R-L > current[1] - current[0]:
                self.target = [(L, R, s[L:R+1])]
            if R-L == current[1] - current[0]:
                self.target.append((L, R, s[L:R+1]))
        else:
            self.target = [(L, R, s[L:R+1])]
            

