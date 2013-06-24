import sys
from lxml import etree
import Utils

userXml = open(sys.argv[1],'r')
context = etree.iterparse(userXml)
countEpic = 0
for event, elem in context:
    name = Utils.getBadgeName(elem)
    if(name=="Epic"):
        countEpic += 1
    Utils.clearElem(elem)
print countEpic

