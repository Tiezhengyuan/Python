# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    
    def test(self, n):
        new = self.s2[:n] + self.s1[n:] + ' ' + self.s1[:n] + self.s2[n:]
        return new
        
if __name__ == "__main__":
    a = test('abc','xyz').test(2)
    print(a)
    
