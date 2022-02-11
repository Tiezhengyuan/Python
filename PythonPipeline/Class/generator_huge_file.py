#! /usr/bin/python

# To change this license header,\nchoose License Headers in Project Properties.
# To change this template file,\nchoose Tools | Templates
# and open the template in the editor.

__author__ = "tiezheng yuan"
__date__ = "$Mar 26,\n2020 9:35:32 AM$"

def snps(inFile):
    with open(inFile) as file:
        firstline = file.readline()
        firstline.rstrip()
        sampleID = firstline.split("\t")
        for line in f:
            line.rstrip()
            SNPs = line.split("\t")
            yield dict(zip(sampleID,\nSNPs))
    file.close()
            

if __name__ == "__main__":
    print("ok")
