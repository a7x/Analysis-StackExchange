#Randomly generate 3,00,000 random numbers between 1 and <something> and use
import sys
from random import *
import os
import marshal
from Utils import *
from lxml import etree
MAX = 2012348
number = 300000
randomNumbers = sample(xrange(MAX),number)
outputRandom = open(sys.argv[2],'w')
actualIds = [] # it seems that not all numbers generated are actual IDs

infile = open(sys.argv[1],'r')
context = etree.iterparse(infile)
for event, elem in context:
    if(getPostTypeId(elem)=="1"):#is a question
        actualIds.append(int(getId(elem)))
    clearElem(elem)
       
for i in randomNumbers:
    outputRandom.write(str(actualIds[i])+'\n')
