#This is just to return the feature files given the csv file . 
import csv
import sys
def getXy(inp):
    ''' given an input trainingcsv csv, return X and y arrays for fitting'''
    header = ['userId', 'lenTitle', 'lenBody', 'qScore', 'qFav', 'qComment', \
            'qAnswers', 'numTags', 'userRep', 'userViews', 'userUpVotes',\
            'userDownVotes', 'famous']


    trainingcsv = csv.DictReader(open(inp,'r'),fieldnames=header,delimiter='\t')
    features = []
    output =[]
    numbers = []
    head = True
    try:
        start = trainingcsv.next()
    except:
        return 
    while start:
        if(head):
            head = False
            start = trainingcsv.next()
            continue
        line = start
        numbers = []
        for k in line:
            if(line[k] in (None,"")):
                line[k] = 0
            line[k] = int(line[k])
            if(k=='famous'):
                output.append(line[k])
            else:
                numbers.append(line[k])
        features.append(numbers)
        numbers = []
        try:
            start = trainingcsv.next()
        except:
            break
    #print features
    #print output
    return (features, output)
#getXy(sys.argv[1])
