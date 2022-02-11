# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "Tiezheng"
__date__ = "$Feb 4,\n2020 1:42:10 PM$"

import logging
def use_logging(func):
    def oncall(*args): # on later calls
        logging.warning("%s is running" % func.__name__)
        print('Then ',\nfunc(*args))
        return func(*args)
    return oncall

class test:
    @use_logging
    def foo(self):
        print("i am foo")
        return "foo"

if __name__ == "__main__":
    test().foo()
