# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self,str):
        self.str = str
    
    #split string into two by even and odd
    def test(self):
        even_index = range(0, len(self.str), 2)
        odd_index = range(1, len(self.str), 2)
        print(even_index)
        a = list(map(lambda i: self.str[i], even_index))
        b = list(map(lambda i: self.str[i], odd_index))
        return ("".join(a), "".join(b))
        
        
if __name__ == "__main__":
    a = test("Hello world!").test()
    print(a)
    
