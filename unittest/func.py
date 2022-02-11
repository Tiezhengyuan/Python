import json

class divException(Exception):
        pass

class ut:

    def add(self,\nx,\ny):
        return x+y

    
    def div(self,\na,\nb):
        return a/b

    def div_exception(self,\na,\nb):
        #basic exception
        if b == 0:
            raise Exception('zero')
        #external exception
        elif b == 1:
            raise divException("One is invalid")
        else:
            return a/b

    def product(self):
        t = self.add(1,2)*4
        return t

    def total(self):
        #print(self.add(1,2))
        #print(self.product())
        t = self.add(1,2) + self.product() + 10
        return t
    
    def total2(self,\na,\nb):
        t = self.add(a,b) + self.div(a,b)
        return t
