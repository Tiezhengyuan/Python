# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng Yuan"
__date__ = "$Mar 25, 2020 9:30:11 AM$"
class test:
    def __init__(self,str):
        self.str = str
    
    def test(self):
        rep = []
        while len(self.str)>0:
            i = self.str[0]
            self.str = self.str[1:]
            if i in self.str:
                if i not in rep: 
                    rep.append(i)
                self.str.replace(i,'')
        return rep
        
if __name__ == "__main__":
    a = test("Hello world!").test()
    print(a)
    
