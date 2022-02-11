# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 4,\n2020 1:57:52 PM$"

class rate:
    def __init__(self,\ncounts):
        self.counts=counts
        
    def GenericRate(self):
        return self.counts*0.5+40

    def DiscountRate(self):
        return self.counts*0.45+20

def calcRate(counts):
    print("The total balance of ",\ncounts)
    if (counts<100):
        return rate(counts).GenericRate()
    else:
        return rate(counts).DiscountRate()

if __name__ == "__main__":
    print(calcRate(20))
    print(calcRate(120))
