# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"

import re
class test:
    def __init__(self,str):
        self.str = str
    
    def test(self):
        words = self.str.split(" ")
        max_word = []
        max_len = 0
        for i in words:
            #remove none letters
            word = re.sub(r'\W', '', i)
            if ( len(word) > max_len ):
                max_word = [word]
                max_len = len(word)            
            elif ( len(word) == max_len ):
                max_word.append(word)
        return (max_word, max_len)
        
if __name__ == "__main__":
    a= test("Hello world! Today is a violent weather.").test()
    print(a)
    
