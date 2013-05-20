import sys
from lxml import etree
from Utils import *

userXml = open(sys.argv[1],'r')
context = etree.iterparse(userXml)
countEpic = 0
for event, elem in context:
    name = getBadgeName(elem)
    if(name=="Epic"):
        countEpic += 1
    clearElem(elem)
print countEpic

