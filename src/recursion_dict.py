class RecursionDict:

    
    def sum_dict(self, mydict):
        """
        return the sum of all the positive numbers 
        in a dictionary which may contain more 
        dictionaries nested in it.
        """
        #print(mydict,t)
        if mydict=={}:
            return []
        else:
            mykeys = list(mydict.keys())
            el = mydict.pop(mykeys[0])
            if isinstance(el, int):
                return [el] + self.sum_dict(mydict)
            elif isinstance(el, dict):
                return self.sum_dict(el) + self.sum_dict(mydict)
            return [] + self.sum_dict(mydict)