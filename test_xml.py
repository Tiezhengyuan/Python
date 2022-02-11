import xml.etree.ElementTree as et
import os




infile = "nyse.xml"
#infile = "test1.txt"
try:
    tree = et.parse(infile)
    root = tree.getroot()
    print(tree)
    print(root.tag, root.attrib)
    print("{:<38s}\t{:<8s}\t{:<8s}\t{:<8s}\t{:<8s}".format(\
        "COMPANY", "LAST", "CHANCE", "MIN", "MAX"))
    print("-"*100)
    for child in root:
        print("{:38s}\t{:<8.3f}\t{:<8.3f}\t{:<8.3f}\t{:<8.3f}".format(\
            child.text, float(child.attrib['last']), \
            float(child.attrib['change']), float(child.attrib['min']), \
            float(child.attrib['max'])))
except FileNotFoundError as e:
    print('no file: ', e) 
except et.ParseError as e:
    print('wrong xml: ', e)
