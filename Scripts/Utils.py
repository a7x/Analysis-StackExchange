import operator
def getUserInfo(elem):
    ''' id, upvotes, downvotes, views, reputation
    '''
    return (getId(elem), getupvotes(elem), getdownvotes(elem), getViews(elem),\
    getReputation(elem))

def topN(d,n):
    return dict(sorted(d.iteritems(), key = operator.itemgetter(1), reverse=True)[:n])

def getViews(elem):
    return elem.get("Views")

def getAcceptedId(elem):
    return elem.get("AcceptedAnswerId")

def getReputation(elem):
    return elem.get("Reputation")

def getId(elem):
    return elem.get("Id")

def getCreationDate(elem):
    return elem.get("CreationDate")

def getParent(elem):
    return elem.get("ParentId")

def getPostTypeId(elem):
    return elem.get("PostTypeId")

def getOwner(elem):
    return elem.get("OwnerUserId")

def getViewCount(elem):
    return int(elem.get("ViewCount"))

def getupvotes(elem):
    return elem.get("UpVotes")

def getdownvotes(elem):
    return elem.get("DownVotes")

def getTitle(elem):
    return elem.get("Title")

def getBody(elem):
    return elem.get("Body")

def getScore(elem):
    return elem.get("Score")

def getFavouriteCount(elem):
    if(elem.get("FavouriteCount") is not None):
        return elem.get("FavouriteCount")
    return 0

def getCommentCount(elem):
    if(elem.get("CommentCount") is not None):
        return elem.get("CommentCount")
    return 0

def getAnswerCount(elem):
    return elem.get("AnswerCount")

def getTags(elem):
    return elem.get("Tags")

def getBadgeName(elem):
    return elem.get("Name")

def getBadgeHolder(elem):
    return elem.get("UserId")

def clearElem(elem):
    elem.clear()
    if elem.getprevious() is not None:
        del elem.getparent()[0]
