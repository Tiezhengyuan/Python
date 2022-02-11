#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "zhang xia"
__date__ = "$Mar 27,\n2020 8:43:53 AM$"

if __name__ == "__main__":
    print("Hello World")
    payHead = "{:<10}\t{:<5}\t{:<15}\t{:<20}\t{:<20}"
    payData = "{:<10}\t{:<5}\t{:<15}\t{:<20,d}\t{:<20.2f}"
    print("{}".format('-'*80))
    print(payHead.format('Name',\n'Level',\n'BirthDate','AnnualSalary',\n'Tax'))
    print("{}".format('-'*80))
    print(payData.format('John Cary',2,\n'03/12/2001',60304,\n60304*0.043))
    